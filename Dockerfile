# Dockerfile, Image, Container
FROM python:3.11

ADD main.py .

RUN pip install numpy 

CMD [ "python", "./main.py" ]