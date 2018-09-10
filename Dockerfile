FROM ubuntu:16.04
RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  libmysqlclient-dev \
  ffmpeg \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip
ENV PYTHONUNBUFFERED 1
RUN mkdir /project
WORKDIR /project
ADD requirements.txt /project/
RUN pip3 install -r requirements.txt
ADD . /project/