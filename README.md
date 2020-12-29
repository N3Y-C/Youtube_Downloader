# Youtube Downloader
>Simple descargador de videos de Youtube hecho en Python

## REQUISITOS

 1. Tener instalado [Python](https://www.python.org/downloads/)
 2. Tener instalado [pytube](https://pypi.org/project/pytube/)
	>pip install pytube

## MODO DE USO
1. Abrir la consola e ir al directorio en donde tengan el archivo YT.py
2. Ejecutar el archivo YT.py

       python YT.py



3. Cuando solicite la url tiene que ingresarse en el siguiente formato

       https://www.youtube.com/watch?v=xxxxxxxxxx

4. Luego se le presentara una lista con distintas calidades, formatos, etc, del video ... buscan el formato y calidad que desean, y en la parte izquiera hay una parte que dice "itag" el cual tendra un valor. Solo ingresan el numero
     
       Ejemplo:
       
       <Stream: itag="137" mime_type="video/mp4" res="1080p" fps="30fps" vcodec="avc1.640028" progressive="False" type="video">
       <Stream: itag="248" mime_type="video/webm" res="1080p" fps="30fps" vcodec="vp9" progressive="False" type="video">
       <Stream: itag="136" mime_type="video/mp4" res="720p" fps="30fps" vcodec="avc1.4d4016" progressive="False" type="video">
       <Stream: itag="247" mime_type="video/webm" res="720p" fps="30fps" vcodec="vp9" progressive="False" type="video">
       
       Ingresa el itag seleccionado : 137
5. Luego se le pedira el lugar donde quieren que se descargue el video, para ello lo ingresaran en el siguiente formato
          
       Ejemplo:
       
       C:\Users\N3Y-C\Videos\DescargasYoutube

6. Solo esperan a que se descargue y listo



### PD:

    Lamentablemente aun no implemento una barra de progreso por ello si se queda un tiempo pegado no se preocupen que es normal.
