import psycopg2
from decimal import Decimal
import datetime

conn = psycopg2.connect(
    host="localhost",
    database="first_database",
    user="postgres",
    password="root",
    port=5432,
)

cur = conn.cursor()

mogrified = cur.mogrify("SELECT %s, %s, %s;", (None, True, False))
mogrified_1 = cur.mogrify("SELECT %s, %s, %s, %s;", (10, 10, 10.0, Decimal("10.00")))

print(mogrified_1)

print(conn.encoding)

# cur.execute("SELECT first_name FROM employee WHERE id =74")
# x = cur.fetchone()
# print(x, type(x), repr(x))
# conn.set_client_encoding('LATIN9')

dt = datetime.datetime.now()
print(dt)

mogrified_2 = cur.mogrify("SELECT %s, %s, %s;", (dt, dt.date(), dt.time()))
print(mogrified_2)

mogrified_3 = cur.mogrify("SELECT %s;", (dt - datetime.datetime(2010, 1, 1),))
print(mogrified_3)

mogrified_4 = cur.mogrify("SELECT %s;", ([10, 20, 30],))
print(mogrified_4)

ids = [10, 20, 30]
cur.execute("SELECT * FROM employee where id = ANY(%s);", (ids,))
rows = cur.fetchall()
for r in rows:
    print(r)

mogrified_5 = cur.mogrify("SELECT %s IN %s;", (10, (10, 20, 30)))
print(mogrified_5)

cur.close()
conn.close()
