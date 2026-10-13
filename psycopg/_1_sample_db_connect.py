import psycopg2

# connect to db
conn = psycopg2.connect(
    host="localhost",
    database="first_database",
    user="postgres",
    password="root",
    port=5432,
)

# cursor
cur = conn.cursor()

cur.execute(
    "INSERT INTO employee (id, first_name, last_name, salary) VALUES(%s, %s, %s, %s)",
    (1001, "Bob", "Odenkirk", 1000000),
)

# execute
cur.execute("SELECT id, first_name FROM employee OFFSET 990 LIMIT 11")

rows = cur.fetchall()

for r in rows:
    print(f"id: {r[0]}, first name: {r[1]}")

# commit the connection, if changes made
conn.commit()

# close the cursor
cur.close()

# close the connection
conn.close()


# cur.execute(
#     SQL("INSERT INTO {} VALUES (%s)").format(Identifier('table_name')),
#     (val1, val2)
# )

# NEVER USE python string concatenation (+) or parameter interpolation (%) to pass variables to a sql query string

# SQL = "INSERT INTO table VALUES (%s);"
# data = ("O'Reilly", )
# cur.execute(SQL, data)

# path = r'C:\Users\shash\table.tables'
# cur.execute("SELECT * FROM mytable WHERE path LIKE %s ESCAPE ''", (path, ))

# None -> Null
# bool -> bool
# float -> real, double
# int, long -> smallint, integer, bigint
# Decimal -> numeric
# str, unicode -> varchar, text
# date -> date
# time -> time, timetz
# datetime -> timestamp, timestamptz
# timedelta -> interval
# list -> ARRAY
# tuple, namedtuple -> IN Syntax
# dict -> hstore

# cur.mogrify("SELECT %s, %s, %s;", (None, True, False))
