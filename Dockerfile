FROM python:3.8

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /opt/app

WORKDIR /opt/app
RUN pip install pipenv

COPY Pipfile .
COPY Pipfile.lock .

RUN pipenv install --system

COPY . /opt/app