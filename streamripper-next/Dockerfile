FROM python:3.14-slim

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        cron \
        ffmpeg \
        tzdata \
        ca-certificates \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY src /app/src
COPY entrypoint.sh /app/entrypoint.sh

RUN chmod +x /app/entrypoint.sh

RUN useradd -ms /bin/bash appuser \
  && mkdir -p /var/log/streamripper /var/lib/streamripper /data \
  && chown -R appuser:appuser /var/log/streamripper /var/lib/streamripper /data

ENV PYTHONUNBUFFERED=1

HEALTHCHECK --interval=30s --timeout=5s --start-period=20s --retries=3 \
  CMD ["/usr/local/bin/python", "/app/src/healthcheck.py"]

ENTRYPOINT ["/app/entrypoint.sh"]
