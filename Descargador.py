from pytube import YouTube

def descargar_video():
    try:
        # Solicitar la URL del video de YouTube
        url = input("Introduce la URL del video de YouTube: ")
        # Solicitar la ruta de destino donde se guardará el video
        path_destino = input("Introduce la ruta donde se guardará el video: ")
        # Crear un objeto YouTube con la URL proporcionada
        yt = YouTube(url)
        # Obtener la secuencia de la mejor calidad disponible
        stream = yt.streams.get_highest_resolution()
        # Descargar el video al directorio destino
        stream.download(path_destino)
        print(f'Video descargado en: {path_destino} - en resolución {stream.resolution}')
    except Exception as e:
        print(f'Ocurrió un error: {e}')
# Ejecutar la función para descargar el video
descargar_video()
