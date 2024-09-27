FROM python:3.10.15-alpine

WORKDIR /carford

COPY . /carford

RUN pip install -r requirements.txt 

EXPOSE 8000

CMD ["python", "run.py"]