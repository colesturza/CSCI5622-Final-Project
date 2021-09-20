# syntax=docker/dockerfile:1

FROM python:3

ENV PYTHONUNBUFFERED 1

ADD . /web_scrapper
WORKDIR /C

COPY requirements.txt /web_scrapper/
RUN pip install -r requirements.txt

COPY src /web_scrapper/

CMD ["python", "main.py"]