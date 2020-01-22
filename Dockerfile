FROM python:3.7.6
ENV PYTHONUNBUFFERED 1

WORKDIR .
COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["sleep", "3"]
CMD ["python3", "./manage.py", "runserver", "0.0.0.0:8000"]