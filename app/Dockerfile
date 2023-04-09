# Dockerfile, Image, Container
FROM python:3.11
EXPOSE 8000
WORKDIR /app
COPY requirements.txt /app
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . /app
ENTRYPOINT ["python3"] 
CMD ["python", "manage.py", "runserver"]