FROM ubuntu:22.04

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y python3 python3-pip python3-venv build-essential libpq-dev

WORKDIR /app
COPY . /app

RUN python3 -m venv venv \
 && . venv/bin/activate \
 && pip install --upgrade pip \
 && pip install -r requirements.txt

EXPOSE 8000
CMD ["sh", "-c", ". venv/bin/activate && python manage.py runserver 0.0.0.0:8000"]
