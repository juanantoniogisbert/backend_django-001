FROM python:3.7.6
ENV PYTHONUNBUFFERED 1

WORKDIR .
COPY requirements.txt .

RUN pip install -r requirements.txt

# CMD [ "sh" ]
# CMD [ "python", "./test.py" ]

EXPOSE 8000

CMD ["python3", "./manage.py", "runserver", "0.0.0.0:8000"]

# CMD ["python3 ./manage.py runserver 0.0.0.0:8000"]