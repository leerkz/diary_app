FROM python:3.12-slim

WORKDIR /app

RUN apt-get update \
    && apt-get install -y gcc libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV SECRET_KEY="django-insecure-z=9*elf5x5@j8z$9lhs2=&l#@s$g1+@7#v-2k7y75c%2mrvzn2"

RUN mkdir -p /app/media

EXPOSE 8000
