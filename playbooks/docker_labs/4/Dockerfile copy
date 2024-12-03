FROM python:3.10.15-slim-bullseye

WORKDIR /app

COPY ./app /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "app.py"]