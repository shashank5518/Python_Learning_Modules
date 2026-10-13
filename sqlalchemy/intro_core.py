from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)

with engine.connect() as conn:
    result = conn.execute(text("select 'Hello World'"))
    print(result.all())

with engine.connect() as conn:
    conn.execute(text("CREATE TABLE table_example (x int, y int)"))
    conn.execute(
        text("INSERT INTO table_example (x, y) VALUES (:x, :y)"),
        [{"x": 1, "y": 1}, {"x": 2, "y": 4}],
    )
    conn.commit()

with engine.begin() as conn:
    conn.execute(
        text("INSERT INTO table_example (x, y) VALUES (:x, :y)"),
        [{"x": 6, "y": 8}, {"x": 9, "y": 10}],
    )

with engine.connect() as conn:
    result = conn.execute(text("SELECT x, y FROM table_example"))
    for row in result:
        print(f"x: {row.x} y: {row.y}")

with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM table_example WHERE y > :y"), {"y": 4})
    for dict_row in result.mappings():
        x = dict_row["x"]
        y = dict_row["y"]
        print(x, y)

with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM table_example"))
    for dict_row in result.mappings():
        x = dict_row["x"]
        y = dict_row["y"]
        print(x, y)

with engine.connect() as conn:
    conn.execute(
        text("INSERT INTO table_example (x, y) VALUES (:x, :y)"),
        [{"x": 11, "y": 12}, {"x": 13, "y": 14}],
    )
    conn.commit()

stmt = text("SELECT x, y FROM table_example WHERE y > :y ORDER BY x, y")
with Session(engine) as session:
    result = session.execute(stmt, {"y": 0})
    for row in result:
        print(f"x: {row.x} y: {row.y}")

with Session(engine) as session:
    result = session.execute(
        text("UPDATE table_example SET y = :y WHERE x = :x"),
        [{"x": 1, "y": 2}, {"x": 13, "y": 15}],
    )
    session.commit()
