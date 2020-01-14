FROM python:3.8

RUN pip install flask
RUN pip install numpy
RUN pip install opencv-python
RUN pip install opencv-contrib-python

ENV FLASK_APP backend/main.py

COPY backend backend

CMD flask run --host=0.0.0.0 --port=80
