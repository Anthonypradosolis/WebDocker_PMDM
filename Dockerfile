FROM python:3

WORKDIR /usr/src/app


COPY holamundo.py .

CMD [ "python", ".holamundo.py" ]
