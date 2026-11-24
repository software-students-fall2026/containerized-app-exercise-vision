FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir pipenv==2024.4.0

COPY Pipfile Pipfile.lock ./

RUN pipenv install --system --deploy

COPY client.py gesture_detector.py ./

EXPOSE 5001

CMD ["python", "client.py"]