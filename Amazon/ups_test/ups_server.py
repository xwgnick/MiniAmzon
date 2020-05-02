import socket
import world_ups_pb2
import amazon_ups_pb2
from google.protobuf.internal.decoder import _DecodeVarint32
from google.protobuf.internal.encoder import _EncodeVarint

def send_request(message, socket):
    serialzied_inf = message.SerializeToString()
    _EncodeVarint(socket.send, len(serialzied_inf), None)
    socket.send(serialzied_inf)

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

world_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
world_socket.connect(("152.3.64.101", 12345))

uconnect = world_ups_pb2.UConnect()
uconnect.isAmazon = False

serialzied_inf = uconnect.SerializeToString()
_EncodeVarint(world_socket.send, len(serialzied_inf), None)
world_socket.send(serialzied_inf)

var_int_buff = []
while True:
    buf = world_socket.recv(1)
    var_int_buff += buf
    msg_len, new_pos = 0, 0
    try:
        msg_len, new_pos = _DecodeVarint32(var_int_buff, 0)
    except IndexError:
        pass
    if new_pos != 0:
        break
whole_message = world_socket.recv(msg_len)

uconnected = world_ups_pb2.UConnected()
uconnected.ParseFromString(whole_message)

print(f'Is UPS connected? {uconnected.result} It is connected to world {uconnected.worldid}!')


amazon_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
amazon_socket.connect(("152.3.64.101", 65535))

ua_world_built = amazon_ups_pb2.UAWorldBuilt()
ua_world_built.worldid = uconnected.worldid
ua_world_built.seqnum = 0

serialzied_inf = ua_world_built.SerializeToString()
_EncodeVarint(amazon_socket.send, len(serialzied_inf), None)
amazon_socket.send(serialzied_inf)

while True:
    amazon_request = receive_response(amazon_socket)
    aucommands = amazon_ups_pb2.AUCommands()
    aucommands.ParseFromString(amazon_request)
    if len(aucommands.requests) != 0:
        aureqtruck = aucommands.requests[0]
        shipid = aureqtruck.shipid
        print("received truck request for order: ", shipid)
        ucommands = world_ups_pb2.UCommands()
        ugopickup = ucommands.pickups.add()
        ugopickup.truckid = 1
        ugopickup.whid = 0
        ugopickup.seqnum = 3
        send_request(ucommands, world_socket)

        world_response = receive_response(world_socket)
        uresponses = world_ups_pb2.UResponses()
        uresponses.ParseFromString(world_response)

        ufinished = uresponses.completions[0]
        uacommands = amazon_ups_pb2.UACommands()
        uatruckarrived = uacommands.truckarrived.add()
        uatruckarrived.truckid = ufinished.truckid
        uatruckarrived.shipid = shipid
        uatruckarrived.seqnum = 0
        print("sending truck arrived to amazon...")
        send_request(uacommands, amazon_socket)
        print("Truck arrived sent")

amazon_socket.close()
