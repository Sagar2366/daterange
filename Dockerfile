FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY daterange_service/ daterange_service/
COPY tests/ tests/
COPY Makefile README.md ./

EXPOSE 8000

CMD ["uvicorn", "daterange_service.app:app", "--host", "0.0.0.0", "--port", "8000"]
