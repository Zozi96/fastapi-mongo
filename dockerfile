FROM public.ecr.aws/lambda/python:3.9

ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

COPY app .

RUN pip install -r requirements.txt

CMD [ "app.asgi.handler" ]
