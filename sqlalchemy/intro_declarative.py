from typing import List

from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    Session,
    aliased,
    mapped_column,
    relationship,
)

from sqlalchemy import (
    ForeignKey,
    String,
    and_,
    create_engine,
    func,
    insert,
    or_,
    select,
)

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user_account"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[str | None]

    addresses: Mapped[List["Address"]] = relationship(back_populates="user")

    def __repr__(self) -> str:
        return f"User(id = {self.id!r}, name = {self.name!r}, fullname = {self.fullname!r})"


class Address(Base):
    __tablename__ = "address"
    id: Mapped[int] = mapped_column(primary_key=True)
    email_address: Mapped[str] = mapped_column(String, nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))

    user: Mapped[User] = relationship(back_populates="addresses")

    def __repr__(self) -> str:
        return f"Address(id = {self.id!r}, email_address = {self.email_address!r})"


# print(Base.metadata)
# print(Base.registry)

Base.metadata.create_all(engine)


with Session(engine) as session:
    sandy = User(name="sandy", fullname="Sandy Cheeks")
    spongebob = User(name="spongebob", fullname="spongebob squarepants")
    session.add_all([sandy, spongebob])
    session.commit()


stmt = select(User).where(User.name == "spongebob")
with Session(engine) as session:
    for row in session.execute(stmt):
        print(row)

    # row = session.execute(select(User)).first()
    # print(row[0])

    row = session.execute(select(User.name, User.fullname)).first()
    print(row)
# print(select(User))

print(
    select(Address.email_address).where(
        and_(
            or_(User.name == "squidward", User.name == "sandy"),
            Address.user_id == User.id,
        )
    )
)

print(select(User).filter_by(name="spongebob", fullname="spongebob squarepants"))

print(select(User).order_by(User.fullname.desc()))

with engine.connect() as conn:
    result = conn.execute(
        select(User.name, func.count(Address.id).label("count"))
        .join(Address)
        .group_by(User.name)
        .having(func.count(Address.id) > 1)
    )
    print(result.all())

address_alias_1 = aliased(Address)
address_alias_2 = aliased(Address)

print(
    select(User)
    .join_from(User, address_alias_1)
    .where(address_alias_1.email_address == "patric@aol.com")
    .join_from(User, address_alias_2)
    .where(address_alias_2.email_address == "patrick@gmail.com")
)

subq = select(Address).where(~Address.email_address.like("%@aol.com")).subquery()
address_subq = aliased(Address, subq)

stmt = (
    select(User, address_subq)
    .join_from(User, address_subq)
    .order_by(User.id, address_subq.id)
)
with Session(engine) as session:
    for user, address in session.execute(stmt):
        print(f"{user} {address}")
