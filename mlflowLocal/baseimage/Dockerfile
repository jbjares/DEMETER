# docker build -t ubuntu1604py37
FROM ubuntu:16.04

RUN apt-get update && \
  apt-get install -y software-properties-common vim && \
  add-apt-repository ppa:deadsnakes/ppa
  #add-apt-repository ppa:fkrull/deadsnakes/python-3.7
RUN apt-get update -y

RUN apt-get install -y build-essential python3.6 python3.7-dev python3-pip python3.7-venv && \
        apt-get install -y git

# update pip
RUN python3.7 -m pip install pip --upgrade && \
        python3.7 -m pip install wheel
