import psycopg2

def delete():
    conn = psycopg2.connect(database = 'wx50db', user = 'wx50', password = 'wx50', host = 'db', port = '5432')
    cur = conn.cursor()
    cur.execute("DELETE FROM amazonapp_purchasedproduct")
    cur.execute("DELETE FROM amazonapp_order")
    cur.execute("DELETE FROM amazonapp_cart")
    cur.execute("DELETE FROM amazonapp_warehouse")
    conn.commit()