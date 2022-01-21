# última imagen oficial ligera de python 3.10.2
FROM python:3.10.2-alpine

# para reflejar en docker donde se trabajará
WORKDIR /usr/src/django-app

# variables de entorno
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# dependencias necesarias
RUN apk update && apk add python3-dev \
                        gcc \
                        musl-dev \
                        libffi-dev
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copiar proyecto
COPY . .