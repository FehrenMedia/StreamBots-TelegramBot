# Dockerfile, Image, Container

FROM python:3.8-slim-buster

WORKDIR /app

ENV mqtt_username=None
ENV mqtt_password=None
ENV mqtt_hostname=None
ENV telegram_toke=None

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "./main.py"]