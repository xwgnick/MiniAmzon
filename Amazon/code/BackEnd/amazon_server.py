import socket
import psycopg2
import amazon_ups_pb2
from threading import Lock
import world_amazon_pb2
import multiprocessing
import concurrent.futures
from google.protobuf.internal.decoder import _DecodeVarint32
from google.protobuf.internal.encoder import _EncodeVarint
import time
from delete_all_tabels import delete

delete()

acks = set()
seq_num = 0
auseq_num = 0
# product_id =0

lock_auseq = Lock()
lock_seq = Lock()
# lock_pid = Lock()
lock_ack = Lock()

HOST = socket.gethostbyname(socket.gethostname())
def send_request(message, socket):
    serialzied_inf = message.SerializeToString()
    _EncodeVarint(socket.send, len(serialzied_inf), None)
    socket.send(serialzied_inf)

def send_world_request(message, socket, seq):
    send_request(message, socket)
    while True:
        # print(""acks)
        time.sleep(2)
        if seq in acks:
            return 
        send_request(message, socket)
        
def receive_response(socket):
    var_int_buff = []
    while True:
        buf = socket.recv(1)
        var_int_buff += buf
        msg_len, new_pos = 0, 0
        try:
            msg_len, new_pos = _DecodeVarint32(var_int_buff, 0)
        except IndexError:
            pass
        if new_pos != 0:
            break
    whole_message = socket.recv(msg_len)
    return whole_message

def receive_frontend_request():
    front_end_request = ""
    bit = front_end_socket.recv(1)
    bit = bit.decode()
    while bit != "\n":
        front_end_request += bit
        bit = front_end_socket.recv(1)
        bit = bit.decode()
    return front_end_request

# Wait UPS for world id
UPS_init_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
UPS_init_socket.bind(('', 65535))
UPS_init_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
UPS_init_socket.listen()
print("--UPS Initialize-- listening from UPS...")
UPS_socket, UPS_ip = UPS_init_socket.accept()
print(f"--UPS Initialize-- Accepted from UPS! The ip is: {UPS_ip}")

whole_message = receive_response(UPS_socket)
ua_world_built = amazon_ups_pb2.UAWorldBuilt()
ua_world_built.ParseFromString(whole_message)
world_id = ua_world_built.worldid
print(f"--World Initialize-- Connecting to world {world_id}...")
aucommands = amazon_ups_pb2.AUCommands()
aucommands.acks.append(ua_world_built.seqnum)
send_request(aucommands, UPS_socket)

# Use the world id to connect and init one warehouse 
world_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
world_socket.connect(("vcm-12399.vm.duke.edu", 23456))

aconnect = world_amazon_pb2.AConnect()
aconnect.worldid = world_id
a_init_warehouse = aconnect.initwh.add()
a_init_warehouse.id = 0
a_init_warehouse.x = 0
a_init_warehouse.y = 0
aconnect.isAmazon = True

send_request(aconnect, world_socket)
whole_message = receive_response(world_socket)
aconnected = world_amazon_pb2.AConnected()
aconnected.ParseFromString(whole_message)

print("--World Initialize-- ", aconnected.result)

#Connect to frontend
front_end_init_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
front_end_init_socket.bind(('', 65432))
front_end_init_socket.listen()
print("--Frontend Initialize-- listening from front end...")
front_end_socket, front_end_ip = front_end_init_socket.accept()
print(f"--Frontend Initialize-- Accepted from front end! The ip is: {front_end_ip}")

# Connect to database
conn = psycopg2.connect(database = 'wx50db', user = 'wx50', password = 'wx50', host = 'db', port = '5432')
# conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_SERIALIZABLE)
print("--Database Initialize-- Database connected!")
cur = conn.cursor()

def seq_increment():
    global seq_num
    lock_seq.acquire()
    ans = seq_num
    seq_num += 1
    lock_seq.release()
    return ans

def auseq_increment():
    global auseq_num
    lock_auseq.acquire()
    ans = auseq_num
    auseq_num += 1
    lock_auseq.release()
    return ans

def send_purchase_command(product_name, product_count):
    acommand = world_amazon_pb2.ACommands()
    a_purchase_more = acommand.buy.add()
    a_purchase_more.whnum = 0
    a_product = a_purchase_more.things.add()
    cur.execute("SELECT product_id FROM amazonapp_warehouse WHERE product_name = %s", (product_name,))
    rows = cur.fetchall()
    ans = 0
    if len(rows) == 0:
        # pid = pid_increment()
        # ans = pid
        cur.execute("INSERT INTO amazonapp_warehouse (product_name, total_number) VALUES (%s, %s)", (product_name, 0))
        cur.execute("SELECT product_id FROM amazonapp_warehouse WHERE product_name = %s", (product_name,))
        rows = cur.fetchall()
        conn.commit()
    a_product.id = rows[0][0]
    a_product.description = product_name
    a_product.count = product_count
    a_purchase_more.seqnum = seq_increment()
    send_world_request(acommand, world_socket, a_purchase_more.seqnum)

#Spawn threads
def process_front_end():
    def process_front_end_request(front_end_request):
        request_head = front_end_request.split(":")[0]
        request_body = front_end_request.split(":")[1]
        if request_head == "purchase more":
            product_name = request_body.split("-")[0]
            needed_count = int(request_body.split("-")[1])
            cur.execute("SELECT total_number FROM amazonapp_warehouse WHERE product_name = %s", (product_name,))
            rows = cur.fetchall()
            if len(rows) == 0 or rows[0][0] < needed_count:
                purchasing_count = needed_count * 10
                print(f"--World Request-- Purchasing {purchasing_count} {product_name} to the warehouse...") 
                send_purchase_command(product_name, purchasing_count)  
            else:
                print(f"--Database Update-- Inventory of {needed_count} {product_name}(s) is enough!")

        if request_head == "new order":
            body = request_body.split("-")
            product_counts = body[:-3]
            x = body[-3]
            y = body[-2]
            ups_name = body[-1]
            user = int(product_counts[0])
            product_counts = product_counts[1:]
            order_products = []
            order_products_count = []
            total_numbers = []
            for product_count in product_counts:
                product_name = product_count.split(",")[0]
                product_count = int(product_count.split(",")[1])
                cur.execute("SELECT total_number FROM amazonapp_warehouse WHERE product_name = %s AND total_number >= %s", (product_name, product_count))
                rows = cur.fetchall()
                order_products.append(product_name)
                order_products_count.append(product_count)
                total_numbers.append(rows[0][0])
            
            cur.execute("INSERT INTO amazonapp_order (owner_id, status, order_description, x, y, ups_name) VALUES (%s, %s, %s, %s, %s, %s)", (user, "ordered", "Order Description: ", x, y, ups_name))
            cur.execute("SELECT shipid FROM amazonapp_order WHERE status = %s AND order_description = %s AND owner_id = %s", ("ordered", "Order Description: ", user))
            shipids = cur.fetchall()
            shipids.sort()
            shipid = shipids[-1][-1]
            order_description = "Order Description: "
            for (i, order_product) in enumerate(order_products):
                cur.execute("UPDATE amazonapp_warehouse set total_number = %s WHERE product_name = %s", (total_numbers[i] - order_products_count[i], order_product))
                cur.execute("DELETE FROM amazonapp_cart WHERE userid_id = %s AND product_name = %s", (user, order_product))
                cur.execute("SELECT product_id FROM amazonapp_warehouse WHERE product_name = %s", (order_product,))
                rows = cur.fetchall()
                order_description += str(order_products_count[i]) + order_product + ", "
                cur.execute("INSERT INTO amazonapp_purchasedproduct (count, product_id_id, shipid_id) VALUES (%s, %s, %s)", (order_products_count[i], rows[0][0], shipid))
                conn.commit()
            order_description = order_description[:-2]
            cur.execute("UPDATE amazonapp_order set order_description = %s WHERE shipid = %s", (order_description, shipid))
            conn.commit()
            order_succeed_response = "Order succeed: all products are ordered!\n"
            print("--Frontend Response-- Order suceed! Sending response to the frontend...")
            front_end_socket.send(order_succeed_response.encode())
            print("--World Request-- Sending to pack command for this order to the world...")
            acommand = world_amazon_pb2.ACommands()
            acommand.simspeed = 30000
            apack = acommand.topack.add()
            apack.whnum = 0
            apack.shipid = shipid
            apack.seqnum = seq_increment()
            for (i, order_product) in enumerate(order_products):
                aproduct = apack.things.add()
                cur.execute("SELECT product_id FROM amazonapp_warehouse WHERE product_name = %s", (order_product,))
                rows = cur.fetchall()
                aproduct.id = rows[0][0]
                aproduct.description = order_product
                aproduct.count = order_products_count[i]
            send_world_request(acommand, world_socket, apack.seqnum)
                
        
    while True:
        with concurrent.futures.ThreadPoolExecutor() as executor_front_end:
            front_end_request = receive_frontend_request()
            print("front end request", front_end_request)
            f = executor_front_end.submit(process_front_end_request, front_end_request)

def process_world():
    def process_world_response(world_response):
        aresponses = world_amazon_pb2.AResponses()
        aresponses.ParseFromString(world_response)
        acommand = world_amazon_pb2.ACommands()
        if len(aresponses.acks) != 0:
            lock_ack.acquire()
            for ack in aresponses.acks:
                acks.add(ack)
            lock_ack.release()

        if len(aresponses.error) != 0:
            for err in aresponses.error:
                print(f"World erro: {aresponses.err}")

        if len(aresponses.arrived) != 0:
            warehouse_ids = []
            products = []
            counts = []
            for purchase_more in aresponses.arrived:
                warehouse_ids.append(purchase_more.whnum)
                for thing in purchase_more.things:
                    products.append(thing.description)
                    counts.append(thing.count)
                acommand.acks.append(purchase_more.seqnum)
                print(f"--World Response-- {thing.count} {thing.description}(s) are purchased from world!")

            for (i, product) in enumerate(products):
                cur.execute("SELECT total_number FROM amazonapp_warehouse WHERE product_name = %s", (product, ))
                current_count = cur.fetchall()
                current_count = current_count[0][0]
                cur.execute("UPDATE amazonapp_warehouse set total_number = %s WHERE product_name = %s", (current_count + counts[i], product))
                conn.commit()

        if len(aresponses.ready) != 0:
            aucommands = amazon_ups_pb2.AUCommands()
            for order in aresponses.ready:
                print(f"order {order.shipid} is packed!")
                aureqtruck = aucommands.requests.add()
                auorder = aureqtruck.orders
                cur.execute("SELECT order_description, x, y, ups_name FROM amazonapp_order WHERE shipid = %s", (order.shipid,))
                rows = cur.fetchall()
                auorder.description = rows[0][0]
                auorder.username = rows[0][3]
                auorder.locationx = int(rows[0][1])
                auorder.locationy = int(rows[0][2])
                aureqtruck.warehouseid = 0
                aureqtruck.shipid = order.shipid
                aureqtruck.seqnum = auseq_increment()
                acommand.acks.append(order.seqnum)
            print("--UPS Request-- Requesting a truck from UPS...")
            send_request(aucommands, UPS_socket)

        if len(aresponses.loaded) != 0:
            aucommands = amazon_ups_pb2.AUCommands()
            for loaded_order in aresponses.loaded:
                print(f"order {loaded_order.shipid} is loaded!")
                acommand.acks.append(loaded_order.seqnum)
                cur.execute("SELECT truckid FROM amazonapp_order WHERE shipid = %s", (loaded_order.shipid,))
                rows = cur.fetchall()
                truckid = rows[0][0]
                autruckLoaded = aucommands.truckloaded.add()
                autruckLoaded.truckid = truckid
                autruckLoaded.shipid = loaded_order.shipid
                autruckLoaded.seqnum = auseq_increment()
                print(f"--UPS Request-- Request delivering for loaded ship {loaded_order.shipid} by truck {truckid}...")
                cur.execute("UPDATE amazonapp_order set status = 'delivering' WHERE shipid = %s", (loaded_order.shipid,))
                conn.commit()
            send_request(aucommands, UPS_socket)

        send_request(acommand, world_socket)

    while True:
        with concurrent.futures.ThreadPoolExecutor() as executor_world:
            world_response = receive_response(world_socket)
            # print("we have world response", world_response)
            f = executor_world.submit(process_world_response, world_response)

def process_UPS():
    def process_UPS_commands(UPS_commands):
        uacommands = amazon_ups_pb2.UACommands()
        uacommands.ParseFromString(UPS_commands)
        aucommands = amazon_ups_pb2.AUCommands()
        if len(uacommands.truckarrived) != 0:
            acommands = world_amazon_pb2.ACommands()
            for truck in uacommands.truckarrived:
                to_load = acommands.load.add()
                to_load.whnum = 0
                to_load.truckid = truck.truckid
                to_load.shipid = truck.shipid
                cur.execute("UPDATE amazonapp_order set truckid = %s WHERE shipid = %s", (truck.truckid, truck.shipid))
                to_load.seqnum = seq_increment()
                aucommands.acks.append(truck.seqnum)
            send_world_request(acommands, world_socket, to_load.seqnum)

        if len(uacommands.packagearrived) != 0:
            for arrived_package in uacommands.packagearrived:
                package_id = arrived_package.shipid
                print(f"package {package_id} is arrived!")
                aucommands.acks.append(arrived_package.seqnum)
                cur.execute("UPDATE amazonapp_order set status = 'delivered' WHERE shipid = %s", (package_id,))
                conn.commit()
        
        send_request(aucommands, UPS_socket)
        

    while True:
        with concurrent.futures.ThreadPoolExecutor() as executor_UPS:
            UPS_commands = receive_response(UPS_socket)
            f = executor_UPS.submit(process_UPS_commands, UPS_commands)


with concurrent.futures.ThreadPoolExecutor() as executor_main:
    front_end_thread = executor_main.submit(process_front_end)
    world_thread = executor_main.submit(process_world)
    UPS_thread = executor_main.submit(process_UPS)
