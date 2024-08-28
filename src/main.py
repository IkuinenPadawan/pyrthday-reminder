from datetime import datetime, date
from sqlalchemy import create_engine, select, text
import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

load_dotenv()
today = date.today()

engine = create_engine(os.getenv("DB_ENGINE_URL"))

def has_birthday_today(birthday):
    return today.month == birthday.month and today.day == birthday.day

def construct_email_message(first_name):
    sender = os.getenv("EMAIL_FROM_ADDRESS")
    recipient = os.getenv("EMAIL_TO_ADDRESS")
    password = os.getenv("EMAIL_PASSWORD")
    subject = "Birthday"
    body = f"Today is {first_name}'s birthday!"
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient
    return msg

def send_email_with_smtp(msg):
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(os.getenv("EMAIL_FROM_ADDRESS"), os.getenv("EMAIL_PASSWORD"))
        smtp_server.sendmail(msg['From'], msg['To'], msg.as_string())

def fetch_people(engine):
    with engine.connect() as connection:
        result = connection.execute(text("SELECT * FROM persons;"))

        for row in result:
            (person_id, first_name, birthday) = row
            yield person_id, first_name, birthday

def check_and_send_birthday_notification():
    for _, first_name, birthday in fetch_people(engine):
        if has_birthday_today(birthday):
            email_message = construct_email_message(first_name)
            send_email_with_smtp(email_message)

def main():
    check_and_send_birthday_notification()

if __name__ == "__main__":
    main()
