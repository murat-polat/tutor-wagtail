FROM ubuntu:20.04

LABEL MAINTAINER=MP
RUN apt-get update && apt-get -y upgrade

RUN apt-get -y install python3-dev default-libmysqlclient-dev build-essential nano vim telnet

RUN apt-get -y install python3-pip  git curl 
RUN pip3 install mysqlclient

RUN mkdir /openedx  openedx/wagtail


RUN pip3 install wagtail uwsgi

## Here you can add your custom Wagtail repository
RUN git clone https://github.com/murat-polat/app 

RUN cd /app

WORKDIR /app/app

RUN pip3 install -r requirements.txt

#RUN python3 manage.py migrate


EXPOSE 8000

CMD uwsgi \
    --http 0.0.0.0:8000 \
    --thunder-lock \
    --single-interpreter \
    --enable-threads \
    --processes=2 \
    --wsgi-file app/wsgi.py

