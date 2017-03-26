 FROM python:2.7
 MAINTAINER patricia@badgermapping.com
 ENV PYTHONUNBUFFERED 1
 RUN mkdir /app
 WORKDIR /app
 ADD requirements.txt /app/
 RUN pip install -r requirements.txt
 ADD . /app/