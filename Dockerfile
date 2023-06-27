FROM python:3.11.2 AS builder

WORKDIR /app

COPY requirements.txt /tmp/requirements.txt

RUN set -ex \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -r /tmp/requirements.txt

COPY . /app


FROM python:3.11.2

WORKDIR /app

COPY --from=builder /app /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 8000