# syntax=docker/dockerfile:1

FROM python:3

ENV PYTHONUNBUFFERED 1

ADD . /webscraper
WORKDIR /webscraper

COPY requirements.txt /webscraper/
RUN pip install -r requirements.txt

COPY . /webscraper/

CMD ["python", "main.py"]