FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY app_root /app/app_root
COPY docker-entrypoint.sh /app/docker-entrypoint.sh
COPY docker-entrypoint-prod.sh /app/docker-entrypoint-prod.sh

RUN sed -i 's/\r$//' /app/docker-entrypoint.sh \
    && sed -i 's/\r$//' /app/docker-entrypoint-prod.sh \
    && chmod +x /app/docker-entrypoint.sh /app/docker-entrypoint-prod.sh

WORKDIR /app/app_root
