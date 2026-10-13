# from typing import Optional
from typing import NewType
from dataclasses import dataclass
import random

name: str = "Corey"
age: int = 38
RGB = NewType("RGB", tuple[int, int, int])
HSL = NewType("HSL", tuple[int, int, int])

# class User(TypedDict):
#     first_name: str
#     last_name: str
#     email: str
#     age: int | None
#     fav_color: RGB | None


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    age: int | None = None
    fav_color: RGB | None = None


# type User = dict[str, str | int | RGB | None]


def create_user(
    first_name: str,
    last_name: str,
    age: int | None = None,
    fav_color: RGB | None = None,
) -> User:
    email = f"{first_name}_{last_name}@example.com".lower()
    # str_age = str(age)
    return User(
        first_name=first_name,
        last_name=last_name,
        email=email,
        age=age,
        fav_color=fav_color,
    )


# T = TypeVar("T")
def random_choice[T](items: list[T]) -> T:
    return random.choice(items)


user1 = create_user("Corey", "Schafer", age=38, fav_color=RGB((109, 123, 145)))
user2 = create_user("Jon", "Snow", fav_color=RGB((206, 10, 48)))

print(user1)
print(user2)

users = [user1, user2]
random_user = random_choice(users)
print(random_user)

emails = [user.email for user in users]
random_email = random_choice(emails)
print(random_email)
