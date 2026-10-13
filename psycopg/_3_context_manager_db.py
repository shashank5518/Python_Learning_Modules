import psycopg2

# with psycopg2.connect(DSN) as conn:
#     with conn.cursor() as cur:
#         cur.execute(QUERY)

# conn = psycopg2.connect(DSN)

# with conn:
#     with conn.cursor() as cur:
#         cur.execute(SQL1)

# with conn:
#     with conn.cursor() as cur:
#         cur.execute(SQL2)

# conn.close()

# conn = psycopg2.connect(DSN)
# try:
#     # connection usage
# finally:
#     conn.close()

# Server side cursor are created in PostgreSQL using the DECLARE command and subsequently handled using MOVE, FETCH and CLOSE commands.
