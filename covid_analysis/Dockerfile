FROM ubuntu:18.04
RUN apt -y update &&\
    apt -y install python3 python3-pip
RUN apt -y install libglib2.0-0
RUN apt -y update && apt install -y libsm6 libxext6
RUN apt -y install libsm6 libxrender1 libfontconfig1
RUN python3 -m pip install --upgrade pip
WORKDIR /covid
COPY . /covid
RUN pip install -r requirements.txt


