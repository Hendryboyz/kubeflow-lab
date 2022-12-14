FROM python:3.10-slim

WORKDIR /component
ARG COMPONENT

COPY requirements.txt /component
COPY components/${COMPONENT}/main.py /component

RUN pip install -r requirements.txt
