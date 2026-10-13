from typing import List

from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, relationship

from sqlalchemy import ForeignKey, create_engine, select, update, delete, insert

engine = create_engine(
    "postgresql+psycopg2://postgres:root@localhost:5432/ecommerce", echo=True
)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user_account"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    fullname: Mapped[str | None]

    addresses: Mapped[List["Address"]] = relationship(back_populates="user")

    def __repr__(self) -> str:
        return f"User(id = {self.id!r}, name = {self.name!r}, fullname = {self.fullname!r})"


class Address(Base):
    __tablename__ = "address"

    id: Mapped[int] = mapped_column(primary_key=True)
    email_address: Mapped[str]
    user_id = mapped_column(ForeignKey("user_account.id"))

    user: Mapped[User] = relationship(back_populates="addresses")

    def __repr__(self) -> str:
        return f"Address(id = {self.id!r}, email_address = {self.email_address!r})"


Base.metadata.create_all(engine)

sandy = User(name="sandy", fullname="sandy cheeks")
squidward = User(name="squidward", fullname="squidward tentacles")
krabs = User(name="ehkrabs", fullname="eugene h. krabs")

session = Session(engine)

session.add_all([sandy, squidward, krabs])

session.commit()

some_squidward = session.get(User, 20)
print(some_squidward)

print(some_squidward is squidward)

# sandy = session.execute(select(User.fullname).where(User.id == 28)).scalar_one()
# print(sandy)
# print(sandy in session.dirty)

# stmt = select(User).where(User.id == 58)
# user = session.execute(stmt).scalar_one()

# user.fullname = "sandy squirrel"
# session.commit()

# stmt = update(User).where(User.fullname == "sandy cheeks").values(fullname = "sandy squirrel")
# session.execute(stmt)
# session.commit()

# patrick = session.get(User, 30)
# session.delete(patrick)

session.execute(select(User).where(User.name == "patrick")).first()

u1 = User(name="pkrabs", fullname="Pearl Krabs")
print(u1.addresses)

# stmt = select(User).where(User.id == 61)
# user = session.execute(stmt).scalar_one_or_none()

# session.delete(user)
# session.commit()

# stmt = delete(User).where(User.name == "sandy")
# session.execute(stmt)
# session.commit()

session.execute(
    insert(User).returning(User),
    [
        {"name": "spongebob", "fullname": "Spongebob Squarepants"},
        {"name": "sandy", "fullname": "Sandy Cheeks"},
        {"name": "patrick", "fullname": "Patrick Star"},
        {"name": "squidward", "fullname": "Squidward Tentacles"},
        {"name": "ehkrabs", "fullname": "Eugene H. Krabs"},
    ],
)

users = session.scalars(
    insert(User).returning(User),
    [
        {"name": "spongebob", "fullname": "Spongebob Squarepants"},
        {"name": "sandy", "fullname": "Sandy Cheeks"},
        {"name": "patrick", "fullname": "Patrick Star"},
        {"name": "squidward", "fullname": "Squidward Tentacles"},
        {"name": "ehkrabs", "fullname": "Eugene H. Krabs"},
    ],
)

print(users.all())
session.commit()
