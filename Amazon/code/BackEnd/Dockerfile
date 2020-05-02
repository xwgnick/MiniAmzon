FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /BackEnd
WORKDIR /BackEnd
ADD requirements.txt /BackEnd/
RUN pip install -r requirements.txt
ADD . /BackEnd