FROM python:3.9-slim-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /code

ADD requirements.txt /tmp
RUN pip3 install --no-cache-dir -r /tmp/requirements.txt