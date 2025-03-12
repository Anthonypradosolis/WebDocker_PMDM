from pytube import YouTube
from urllib.error import HTTPError
from pytubefix import YouTube


def Download(link):
    try:
        yt = YouTube(link)
        yt = yt.streams.get_highest_resolution()
        yt.download()
        print("¡Descarga completada con éxito!")
    except HTTPError as e:
        print(f"HTTP Error: {e.code} - {e.reason}")
    except Exception as e:
        print(f"Hubo un error al descargar el video del URL proporcionado: {e}")

link = "https://www.youtube.com/watch?v=9NGgLhEVCUk"
Download(link)