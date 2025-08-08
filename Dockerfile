FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && \
    apt-get install -y \
      netcat-traditional \
      libpq-dev \
      build-essential \
    && pip install --upgrade pip \
    && pip install -r requirements.txt \
    && rm -rf /var/lib/apt/lists

COPY . .
# RUN chmod +x /app/entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]
