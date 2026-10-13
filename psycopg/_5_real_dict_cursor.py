import os

import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_PORT = os.getenv("DB_PORT")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_USER = os.getenv("DB_USER")

with psycopg2.connect(
    host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASSWORD, port=DB_PORT
) as conn:
    with conn.cursor(cursor_factory=RealDictCursor) as cur:
        user_id = "1"
        cur.execute("SELECT * FROM users WHERE id = %s", (user_id))
        row = cur.fetchone()
        print(row["name"])
        cur.execute(
            "INSERT INTO users (name, age, gender, nationality) VALUES (%s, %s, %s, %s) RETURNING id",
            ("Shashank", 23, "male", "India"),
        )
        new_user = cur.fetchone()
        print(new_user["id"])
