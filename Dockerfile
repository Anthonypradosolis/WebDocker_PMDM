FROM python:alpine

WORKDIR /usr/src/app

COPY holamundo.py .

CMD [ "python", "./holamundo.py" ]
