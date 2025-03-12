FROM python:alpine

WORKDIR /usr/src/app

COPY videosyoutube/holamundo.py .

RUN pip install pytubefix
RUN pip install pytube

CMD [ "python", "./holamundo.py" ]
