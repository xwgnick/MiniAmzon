FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /FrontEnd
WORKDIR /FrontEnd
ADD requirements.txt /FrontEnd/
RUN pip install -r requirements.txt
ADD . /FrontEnd