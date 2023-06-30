FROM python:3.11.4-slim-bullseye

USER root
RUN apt-get update && apt-get install

RUN pip install pip==23.1.2 setuptools==68.0.0 wheel==0.40.0

COPY crawler_requirements.txt .
RUN pip install --no-cache -r crawler_requirements.txt

COPY . .

ENV PATH="/app/.local/bin/:${PATH}"

# ENTRYPOINT ["python", "run.py"]
