FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN python -m pip install pip --upgrade &&\
    pip install -r requirements.txt 

EXPOSE 8080

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "main:app"]
