FROM python:3.6.6-alpine3.8
MAINTAINER Felipe Colen <felipecolen@gmail.com>

ENV TZ="America/Porto_Velho"

#RUN apk add --update --no-cache curl bash && apk del bash &&

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip setuptools && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

RUN rm -r /root/.cache

EXPOSE 5000
