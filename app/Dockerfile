# Dockerfile, Image, Container
FROM python:3.11

WORKDIR /app


COPY requirements.txt /app
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt
COPY . /app 


CMD ["python", "manage.py", "runserver", "127.0.0.1:8080"]