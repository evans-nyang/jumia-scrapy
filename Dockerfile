FROM python:3.9

RUN apt-get update && apt-get install

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache -r requirements.txt

ADD . .

WORKDIR /app/jumiascraper

CMD python run.py
