import psycopg2
conn = psycopg2.connect(database = 'wx50db', user = 'wx50', password = 'wx50', host = 'localhost', port = '5432')

cur = conn.cursor()
cur.execute("DELETE FROM amazonapp_warehouse")
cur.execute("DELETE FROM amazonapp_cart")
conn.commit()