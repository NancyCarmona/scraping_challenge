FROM ubuntu:18.04
RUN apt-get update && apt-get install \
  -y --no-install-recommends \
         python3.7 \
         python3-virtualenv \
         python3-pip \
         python-virtualenv \
         python3-dev \
         libmysqlclient-dev \
         python3.6-dev \
         libmysqlclient-dev  \
         python-mysqldb \
         gcc \
         libc-dev \
         wget \
         curl \
         firefox

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

WORKDIR /usr/src/app
COPY requirements.txt requirements.txt

RUN pip3 install setuptools
RUN pip3 install -U selenium
RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz
RUN tar -xvzf geckodriver*
RUN chmod +x geckodriver
RUN  mv geckodriver /usr/local/bin/

RUN  pip3 install -r requirements.txt
COPY . /usr/src/app

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
