FROM python:3.7 AS build
RUN python -m venv /opt/venv
# Make sure we use the virtualenv:
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install mlflow psycopg2 mysqlclient pysftp

FROM python:3.7-slim
COPY --from=build /opt/venv /opt/venv
# Make sure we use the virtualenv:
ENV PATH="/opt/venv/bin:$PATH"
EXPOSE 5000/tcp
ENTRYPOINT [ "mlflow", "server", "--host", "0.0.0.0"]
CMD [ "--backend-store-uri", "sqlite:////mlruns/mlruns.db", \
      "--default-artifact-root", "sftp://foo:pass@193.175.161.65:2222/"]
