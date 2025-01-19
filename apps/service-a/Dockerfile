FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install curl -y
COPY app.py .

CMD ["python", "app.py"]
