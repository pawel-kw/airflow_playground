ARG AIRFLOW_IMAGE_NAME="2.2.5-python3.8"

FROM "apache/airflow:${AIRFLOW_IMAGE_NAME}"

# - Install GCP util
RUN curl -sSL https://sdk.cloud.google.com | bash
ENV PATH $PATH:/home/airflow/google-cloud-sdk/bin

CMD [ "standalone" ]