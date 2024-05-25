FROM python:3.10.12

COPY . /app

WORKDIR /app

RUN python -m pip install pip --upgrade &&\
    pip install --no-cache-dir -r requirements.txt 

EXPOSE 8080

CMD ["gunicorn", "--workers=4", "--bind", "0.0.0.0:8080", "main:app"]
