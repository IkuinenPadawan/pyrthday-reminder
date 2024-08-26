from datetime import datetime, date
from sqlalchemy import create_engine, select, text

today = date.today()

engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost:5432/birthdays")

def is_birthday(birthday):
    return today.month == birthday.month and today.day == birthday.day

with engine.connect() as connection:
    result = connection.execute(text("SELECT * FROM persons;"))

    for row in result:
        (id, first_name, birthday) = row

        if is_birthday(birthday):
            print(f"Today is {first_name}'s birthday!")
