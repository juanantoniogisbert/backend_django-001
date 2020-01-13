FROM python:3.7.6-alpine3.10
ENV PYTHONUNBUFFERED 1

WORKDIR .
COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ['python test.py']

EXPOSE 8000