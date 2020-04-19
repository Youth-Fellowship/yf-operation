FROM python:alpine3.11 AS build

LABEL author="olumide ogundele <olumideralph@gmail.com>"
LABEL version="1.0"
LABEL decription="youth fellowship hymns delivery application"

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

# CMD [ "gunicorn", "-w", "4", "--bind", "0.0.0.0:5000", "wsgi"]

CMD [ "gunicorn", "--bind", "0.0.0.0:5000", "wsgi"]