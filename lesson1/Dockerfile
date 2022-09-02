FROM python:3.8-slim as base

RUN apt-get update && pip3 install --upgrade pip && pip install poetry

WORKDIR /app
COPY pyproject.toml poetry.lock .
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi --no-dev
RUN rm -rf /app

CMD uvicorn app:app --host 0.0.0.0 --reload

