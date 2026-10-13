import psycopg2
from psycopg2 import OperationalError
from psycopg2.extensions import connection as PgConnection


def create_connection(
    host_name: str, db_name: str, user_name: str, user_password: str, db_port: int
) -> PgConnection:
    try:
        connection = psycopg2.connect(
            database=db_name,
            host=host_name,
            user=user_name,
            port=db_port,
            password=user_password,
        )
        print("Connection to PostgreSQL DB Successful")
    except OperationalError as e:
        print(f"'{e}' occured")
    return connection


def create_database(connection: PgConnection, query: str) -> None:
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query Executed Successfully")
    except OperationalError as e:
        print(f"'{e}' occurred")


def execute_query(db_connection: PgConnection, query: str) -> None:
    db_connection.autocommit = True
    cursor = db_connection.cursor()
    try:
        cursor.execute(query)
        print("Query Executed Succesfully")
    except OperationalError as e:
        print(f"'{e}' occurred")


def execute_read_query(db_connection: PgConnection, query: str):
    cursor = db_connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except OperationalError as e:
        print(f"'{e}' occurred")


def close_cursor(cursor):
    cursor.close()


def close_connection(db_connection):
    db_connection.close()


# connection = create_connection("localhost", "postgres", "postgres", "root", 5432)
# create_database_query = "CREATE DATABASE test_psycop"
# create_database(connection, create_database_query)
db_connection = create_connection("localhost", "test_psycop", "postgres", "root", 5432)

create_users_table = """
    CREATE TABLE IF NOT EXISTS users(
        id BIGSERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        gender TEXT NOT NULL,
        nationality TEXT NOT NULL
    )
"""

execute_query(db_connection, create_users_table)

create_posts_table = """
    CREATE TABLE IF NOT EXISTS posts (
        id BIGSERIAL PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT NOT NULL,
        user_id INTEGER REFERENCES users(id)
    )
"""

execute_query(db_connection, create_posts_table)

users = [
    ("James", 25, "male", "USA"),
    ("Leila", 32, "female", "France"),
    ("Brigitte", 35, "female", "England"),
    ("Mike", 40, "male", "Denmark"),
    ("Elizabeth", 21, "female", "Canada"),
]

user_records = ", ".join(["%s"] * len(users))

insert_query_users = (
    f"INSERT INTO users (name, age, gender, nationality) VALUES {user_records}"
)

db_connection.autocommit = True
cursor = db_connection.cursor()
cursor.execute(insert_query_users, users)

posts = [
    ("Happy", "I am feeling very happy today", 1),
    ("Hot Weather", "The weather is very hot today", 2),
    ("Help", "I need some help with my work", 2),
    ("Great News", "I am getting married", 1),
    ("Interesting Game", "It was a fantastic game of tennis", 5),
    ("Party", "Anyone up for a late-night party today?", 3),
]

post_records = ", ".join(["%s"] * len(posts))

insert_query_posts = (
    f"INSERT INTO posts (title, description, user_id) VALUES {post_records}"
)

db_connection.autocommit = True
cursor = db_connection.cursor()
cursor.execute(insert_query_posts, posts)

select_users = "SELECT * FROM users"

cursor.execute("DELETE FROM users WHERE id > 5")
users = execute_read_query(db_connection, select_users)

select_posts = "SELECT * FROM posts"
cursor.execute("DELETE FROM posts WHERE id > 5")
posts = execute_read_query(db_connection, select_posts)

for user in users:
    print(user)

for post in posts:
    print(post)

update_user_query = """
    UPDATE users 
    SET name = 'Eddard'
    WHERE id = 4
"""
execute_query(db_connection, update_user_query)
users = execute_read_query(db_connection, select_users)

for user in users:
    print(user)

close_cursor(cursor)
close_connection(db_connection)
