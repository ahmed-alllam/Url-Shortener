FROM python:3.8-alpine
MAINTAINER Ahmed Emad.
ENV PYTHONUNBUFFERED 1
RUN mkdir /url-shortener
WORKDIR /url-shortener
COPY . /url-shortener
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
      gcc libc-dev linux-headers postgresql-dev \
      && apk add postgresql \
      && pip3 install psycopg2 \
RUN pip3 install -r /url-shortener/requirements.txt
RUN apk del .tmp-build-deps
RUN adduser -D url-shortener
USER url-shortener