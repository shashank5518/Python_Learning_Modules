from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    MetaData,
    String,
    Table,
    and_,
    bindparam,
    create_engine,
    func,
    insert,
    literal_column,
    or_,
    select,
    text,
)

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)

metadata_obj = MetaData()

user_table = Table(
    "user_account",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("name", String(30)),
    Column("fullname", String),
)

print(user_table.c.name)
print(user_table.c.keys())
print(user_table.primary_key)

address_table = Table(
    "address",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("user_id", ForeignKey("user_account.id"), nullable=False),
    Column("email_address", String, nullable=False),
)

metadata_obj.create_all(engine)
# metadata_obj.drop_all(engine)

stmt = insert(user_table).values(name="spongebob", fullname="spongebob squarepants")
print(stmt)

print(stmt.compile().params)

with engine.connect() as conn:
    result = conn.execute(stmt)
    conn.commit()

print(result.inserted_primary_key)

with engine.connect() as conn:
    result = conn.execute(
        insert(user_table),
        [{"name": "sandy", "fulllname": "sandy mandy"}, {"name": "shashank"}],
    )
    conn.commit()

scalar_subq = (
    select(user_table.c.id)
    .where(user_table.c.name == bindparam("username"))
    .scalar_subquery()
)

with engine.connect() as conn:
    result = conn.execute(
        insert(address_table).values(user_id=scalar_subq),
        [
            {"username": "spongebob", "email_address": "spongebob@sqlalchemy.com"},
            {"username": "sandy", "email_address": "sandy@sqlalchemy.com"},
            {"username": "sandy", "email_address": "sandy@squirrelpower.org"},
        ],
    )
    conn.commit()

insert_stmt = insert(address_table).returning(
    address_table.c.id, address_table.c.email_address
)

stmt = select(user_table).where(user_table.c.name == "spongebob")
print(stmt)

with engine.connect() as conn:
    for row in conn.execute(stmt):
        print(row)

print(select(user_table))
print(select(user_table.c.name, user_table.c.fullname))

stmt = select(user_table.c.name).order_by(user_table.c.name)

with engine.connect() as conn:
    for row in conn.execute(stmt):
        print(f"Username: {row.name}")

stmt = select(text("'some phrase'"), user_table.c.name).order_by(user_table.c.name)

with engine.connect() as conn:
    print(conn.execute(stmt).all())

stmt = select(literal_column("'some phrase'").label("p"), user_table.c.name).order_by(
    user_table.c.name
)

with engine.connect() as conn:
    for row in conn.execute(stmt):
        print(f"{row.p}, {row.name}")

print(select(user_table).where(user_table.c.name == "squidward"))
print(
    select(address_table.c.email_address)
    .where(user_table.c.name == "squidward")
    .where(address_table.c.user_id == user_table.c.id)
)

print(
    select(user_table.c.name, address_table.c.email_address).join_from(
        user_table, address_table
    )
)

print(select(user_table.c.name, address_table.c.email_address).join(address_table))

print(select(address_table.c.email_address).select_from(user_table).join(address_table))

print(select(func.count("*")).select_from(user_table))

print(
    select(address_table.c.email_address)
    .select_from(user_table)
    .join(address_table, user_table.c.id == address_table.c.user_id)
)

print(select(user_table).join(address_table, isouter=True))
print(select(user_table).join(address_table, full=True))

count_func = func.count(user_table.c.id)
print(count_func)

user_alias_1 = user_table.alias()
user_alias_2 = user_table.alias()

print(
    select(user_alias_1.c.name, user_alias_2.c.name).join_from(
        user_alias_1, user_alias_2, user_alias_1.c.id > user_alias_2.c.id
    )
)
