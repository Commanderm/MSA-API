# Dockerfile для веб-приложения
FROM python:3.9-slim
LABEL authors="mvolkov"
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "app.py"]