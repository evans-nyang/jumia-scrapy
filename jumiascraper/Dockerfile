FROM python:3.11.4-slim-bullseye

USER root
RUN apt-get update && apt-get install

WORKDIR /usr/app

RUN pip install --upgrade pip setuptools wheel

COPY requirements.txt .
RUN pip install --no-cache -r requirements.txt

COPY . .

# WORKDIR usr/app/jumiascraper

ENV PATH="/app/.local/bin/:${PATH}"

ENTRYPOINT ["python", "run.py"]
