FROM python:3.11-alpine3.17

EXPOSE 5000

ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

COPY app .

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "asgi.py" ]
