FROM python:3.8

COPY backend backend

RUN pip install flask
RUN pip install numpy

CMD ['python', 'backend/main.py']
