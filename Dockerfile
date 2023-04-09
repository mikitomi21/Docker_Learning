# Dockerfile, Image, Container
FROM python:3.8-slim-buster

WORKDIR /app

ENV PYTHONNUNBUFFERED=1

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt