# Dockerfile для микросервиса управления задачами
FROM python:3.9-slim
LABEL authors="mvolkov"
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5001
CMD ["python", "task_service.py"]