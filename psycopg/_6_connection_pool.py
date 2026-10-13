import os
from collections.abc import Generator
from contextlib import contextmanager

import psycopg2
from dotenv import load_dotenv
from psycopg2.extensions import connection
from psycopg2.extras import RealDictCursor
from psycopg2.pool import SimpleConnectionPool

load_dotenv()
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_USER = os.getenv("DB_USER")
DB_PORT = os.getenv("DB_PORT")
pool = SimpleConnectionPool(
    minconn=1,
    maxconn=10,
    host=DB_HOST,
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    port=DB_PORT,
)


@contextmanager
def get_connection(pool) -> Generator[connection, None, None]:
    conn = pool.getconn()
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        pool.putconn(conn)


# conn = pool.getconn()
with get_connection(pool) as conn:
    # try:
    with conn.cursor(cursor_factory=RealDictCursor) as cur:
        user_id = 1
        cur.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        row = cur.fetchall()
        print(row)
# finally:
# pool.putconn(conn)
