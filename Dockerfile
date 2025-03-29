FROM python:3.10-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends libpq-dev gcc && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app
COPY magic /app/magic
COPY quiz /app/quiz

RUN pip install --no-cache-dir -r requirements.txt

RUN chmod -R 755 /app

EXPOSE 8000

CMD ["python", "app.py"]