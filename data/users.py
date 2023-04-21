from dataclasses import dataclass


@dataclass
class User:
    first_name: str
    last_name: str
    full_name: str
    email: str
    gender: str
    phone_number: str
    birth_year: str
    birth_month: str
    birth_day: str
    date_of_birth: str
    subjects: str
    hobbies: str
    photo: str
    address: str
    state: str
    city: str
    state_city: str


def_user = User(
    first_name="User",
    last_name="Default",
    full_name="User Default",
    email="default@mail.com",
    gender="Male",
    phone_number="9111111111",
    birth_year="1991",
    birth_month="November",
    birth_day="03",
    date_of_birth="03 November,1991",
    subjects="Maths",
    hobbies="Sports",
    photo="icon.jpg",
    address="Saint P Nevskiy prospect 111",
    state="NCR",
    city="Delhi",
    state_city="NCR Delhi"
)
