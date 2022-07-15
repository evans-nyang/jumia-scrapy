# First-time build can take upto 10 mins.

FROM apache/airflow:2.2.3

ENV AIRFLOW_HOME=/opt/airflow

USER root
RUN apt-get update -qq && apt-get install vim -qqq
# git gcc g++ -qqq

COPY requirements.txt .
RUN pip install --upgrade pip 
RUN pip install --no-cache-dir -r requirements.txt

# Ref: https://airflow.apache.org/docs/docker-stack/recipes.html

SHELL ["/bin/bash", "-o", "pipefail", "-e", "-u", "-x", "-c"]


ENV AWS_HOME=/home/aws-cloud-sdk

ENV PATH="${AWS_HOME}/bin/:${PATH}"

# RUN DOWNLOAD_URL="https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" \
#     && TMP_DIR="$(mktemp -d)" \
#     && curl -fL "${DOWNLOAD_URL}" --output "${TMP_DIR}/awscliv2.zip" \
#     && mkdir -p "${AWS_HOME}" \
#     && unzip "${TMP_DIR}/awscliv2.zip" -d "${AWS_HOME}" \
#     && "${AWS_HOME}/aws/install" \
#     && rm -rf "${TMP_DIR}" \
#     && aws --version

WORKDIR $AIRFLOW_HOME

COPY scripts scripts
RUN chmod +x scripts

USER $AIRFLOW_UID
