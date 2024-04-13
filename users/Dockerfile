# Dockerfile для микросервиса управления пользователями
FROM python:3.9-slim
LABEL authors="mvolkov"
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5002
CMD ["python", "user_service.py"]