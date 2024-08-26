from datetime import datetime, date
from sqlalchemy import create_engine, select, text
import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

load_dotenv()
today = date.today()

engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost:5432/birthdays")

def is_birthday(birthday):
    return today.month == birthday.month and today.day == birthday.day

def send_email(subject, body, sender, recipient, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, recipient, msg.as_string())
    print("Message sent!")

with engine.connect() as connection:
    result = connection.execute(text("SELECT * FROM persons;"))

    for row in result:
        (id, first_name, birthday) = row

        if is_birthday(birthday):
            print(f"Today is {first_name}'s birthday!")
            subject = "Birthday"
            body = "Today is {} birthday!".format(first_name)
            sender = os.getenv("EMAIL_FROM_ADDRESS")
            recipient = os.getenv("EMAIL_TO_ADDRESS")
            password = os.getenv("EMAIL_PASSWORD")
            send_email(subject, body, sender, recipient, password)

