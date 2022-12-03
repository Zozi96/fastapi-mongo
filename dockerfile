FROM python:3.11-slim-buster

EXPOSE 5000

ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

COPY app .

RUN pip install -r requirements.txt

CMD [ "python", "asgi.py" ]
