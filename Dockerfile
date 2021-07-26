FROM python:3.9-slim
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /app
RUN pip install --upgrade pip
ENV REDIS_CONTAINER TRUE
COPY requirements.txt /app/
RUN pip install -r requirements.txt
