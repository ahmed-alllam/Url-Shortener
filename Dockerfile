FROM python:3.8-alpine
MAINTAINER Ahmed Emad.
ENV PYTHONUNBUFFERED 1
RUN mkdir /Url-Shortener
WORKDIR /Url-Shortener
COPY . /Url-Shortener
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
      gcc libc-dev linux-headers postgresql-dev \
      && apk add postgresql \
      && pip3 install psycopg2 \
RUN pip3 install -r /Url-Shortener/requirements.txt
RUN apk del .tmp-build-deps
RUN adduser -D Url-Shortener
USER Url-Shortener