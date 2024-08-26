from datetime import datetime, date
from sqlalchemy import create_engine, select, text

today = date.today()

engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost:5432/birthdays")
conn = engine.connect()
result = conn.execute(text("SELECT * FROM persons;"))

for row in result:
    (id, first_name, birthday) = row

    if today.month == birthday.month and today.day == birthday.day:
        print(f"Today is {first_name}'s birthday!")
