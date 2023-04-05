# Dockerfile, Image, Container
FROM pyton:3.8

ADD main.py .

RUN pip install numpy 

CMD [ "python", "./main.py" ]