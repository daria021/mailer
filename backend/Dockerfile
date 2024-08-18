FROM python:3.12

RUN mkdir /fastapi_newsletter

WORKDIR /fastapi_newsletter

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY .. .

