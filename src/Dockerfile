FROM python:3.9-alpine

COPY . /app/ 

RUN pip install -r /app/requirements.txt

RUN crontab /app/daily_birthday_check.cron

RUN touch /tmp/out.log

CMD crond && tail -f /tmp/out.log

