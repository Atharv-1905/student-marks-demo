
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --default-timeout=180 -r requirements.txt

COPY hello.py .
COPY tests/ tests/
COPY monitoring/ monitoring/

CMD ["python", "hello.py"]

