FROM ubuntu:18.04

LABEL MAINTAINER=MP
RUN apt-get update && apt-get -y upgrade

RUN apt-get -y install python3-dev default-libmysqlclient-dev build-essential nano vim telnet

RUN apt-get -y install python3-pip  git curl 
RUN pip3 install mysqlclient

RUN mkdir /openedx  openedx/wagtail


RUN pip3 install wagtail gunicorn


RUN wagtail start app && cd /app

WORKDIR /app

RUN pip3 install -r requirements.txt

RUN python3 manage.py migrate


EXPOSE 8000
# Running server
CMD gunicorn --bind=0.0.0.0:8000 --workers 2 --max-requests=1000 app.wsgi:application