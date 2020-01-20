FROM python:3.8

RUN apt-get update
RUN apt install -y tesseract-ocr

RUN pip install flask
RUN pip install flask_cors
RUN pip install numpy
RUN pip install opencv-python
RUN pip install opencv-contrib-python
RUN pip install pytesseract

ENV FLASK_APP backend/main.py

COPY backend backend

CMD flask run --host=0.0.0.0 --port=80
EXPOSE 80