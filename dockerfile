FROM python:3.11-slim-buster

EXPOSE 5000

ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

COPY app .

RUN pip install -r requirements.txt

CMD [ "uvicorn", "asgi:app", "--host", "0.0.0.0", "--port", "5000" ]
