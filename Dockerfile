FROM python:3.8

RUN pip install flask
RUN pip install pymongo
RUN pip install numpy

ENV FLASK_APP backend/main.py

COPY backend backend

CMD flask run
