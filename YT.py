from pytube import YouTube

url = input("Ingresa la url del video : ")
myvideo = YouTube(url)
print("\n")
#Titulo del Video
print("**************************** TITULO ****************************")
print("Titulo del video : "+myvideo.title)
print("\n")

#Miniatura del Video
print("********************** MINIATURA DEL VIDEO **********************")
print(myvideo.thumbnail_url)
print("\n")

#Obtener todas los Streams
print("**************************** ELIGE LA CALIDAD DEL VIDEO ****************************")
calidades = myvideo.streams.all()
for i in calidades:
    print(i)
objetivo = input("Ingresa el itag seleccionado : ")
print("\n")

#Obtener todas los Streams
print("**************************** DESCARGANDO VIDEO ****************************")
lugar = input('Porfavor ingrese el lugar donde se guardara el video : ')
print("DESCARGA INICIADA ....")
print("DESCARGANDO ....")
print("PORFAVOR ESPERE, ESTO TOMARA TIEMPO...")
descarga = myvideo.streams.get_by_itag(objetivo)
descarga.download(lugar)
print("\n")

#Obtener todas los Streams
print("**************************** DESCARGA FINALIZADA ****************************")
print("\n")
