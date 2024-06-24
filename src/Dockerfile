FROM python:3.10

# создаем директорию
RUN mkdir /fastapi_newsletter

# перемещаемся в эту директорию
WORKDIR /fastapi_newsletter

COPY requirements.txt .

RUN pip install -r requirements.txt

# копируем все папки и файлы внутрь образа
COPY . .

#RUN chmod a+x docker/*.sh

#CMD gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000