FROM python:3.10

WORKDIR /consumer/app

COPY check_consumer/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY check_consumer/ .
