import struct
from pathlib import Path
import math
from collections import Counter
import struct
import matplotlib.pyplot as plt


def calcular_entropia(lista_probabilidades):
    entropia = 0.0
    for p in lista_probabilidades:
        if p > 0:  # Evitamos el error matemático de log2(0)
            entropia -= p * math.log2(p)
    return entropia

def verificacion_archivo(xruta, xtipo):
    if xtipo == "wav":
        if not xruta.exists():
            print("La ruta seleccionada no existe.")
            return False
        elif not xruta.is_file():
            print("La ruta no corresponde a un archivo, podria ser un directorio.")
            return False
        elif xruta.suffix.lower() != ".wav":
            print(f"El archivo seleccionado es de tipo {xruta.suffix}. Se esperaba .wav")
            return False
        else:
            print("Archivo WAV cargado correctamente")
            return True
    elif xtipo == "mp3":
        if not xruta.exists():
            print("La ruta seleccionada no existe.")
            return False
        elif not xruta.is_file():
            print("La ruta no corresponde a un archivo, podria ser un directorio.")
            return False
        elif xruta.suffix.lower() != ".mp3":
            print(f"El archivo seleccionado es de tipo {xruta.suffix}. Se esperaba .mp3")
            return False
        else:
            print("Archivo mp3 cargado correctamente")
            return True
        

if __name__ == "__main__":
    #Solicitamos las rutas de los archivos mp3 y WAV respectivamente
    entrada_mp3 = input("Ingresa la ruta del archivo mp3: ")
    entrada_wav = input("Ingresa la ruta del archivo WAV: ")
    ruta_mp3 = entrada_mp3.strip("\"'")
    ruta_wav = entrada_wav.strip("\"'")
    ruta_limpia_mp3 = Path(ruta_mp3)
    ruta_limpia_wav = Path(ruta_wav)
    if verificacion_archivo(ruta_limpia_wav, "wav") and verificacion_archivo(ruta_limpia_mp3, "mp3"):
        archivo_mp3 = open(ruta_limpia_mp3, "rb")
        archivo_wav = open(ruta_limpia_wav, "rb")
        print("ANALISIS DEL ARCHIVO WAV")
        with ruta_limpia_wav.open("rb") as f:
            cabecera = f.read(44)
            chunkId_bytes = struct.unpack(">4s",cabecera[0:4])[0]
            chunkID_text = chunkId_bytes.decode("ascii")
            print(chunkId_bytes)
            if chunkID_text == "RIFF":
                print("Cabecera RIFF valida.")
            else:
                print("Error: No es un archivo RIFF")
            chunkFormat_bytes = struct.unpack(">4s",cabecera[8:12])[0]
            print(f"Formato: {chunkFormat_bytes}")
            chunkSize_bytes = struct.unpack("<4s",cabecera[4:8])[0]
            chunkSize_num = struct.unpack("<I",chunkSize_bytes)[0]
            print(f"Tamaño: {chunkSize_num + 8}")
            chunkSampleRate = struct.unpack("<I",cabecera[24:28])[0]
            print(f"Frecuencia de muestreo: {chunkSampleRate}")
            chunkNumChannels_bytes = struct.unpack("<H",cabecera[22:24])[0]
            print(f"Numero de canales: {chunkNumChannels_bytes}")
            f.close()
        with ruta_limpia_wav.open("rb") as f:
            #Inciso C, creo 256 contadores que son los posibles bytes y los inicializo en 0
            contadores_wav = [0] * 256
            #con un for recorro todo el archivo contando cuantas veces aparece cada byte en el archivo.
            datos_wav = f.read()
            for byte in datos_wav:
                contadores_wav[byte] += 1
            totalbytes_wav = sum(contadores_wav) #cuento el tamaño total del archivo en bytes.
            probabilidades_wav = []
            for i in range(len(contadores_wav)):
                print(f"Probabilidad del byte: {i}, {contadores_wav[i]/totalbytes_wav}")
                probabilidades_wav.append(contadores_wav[i]/totalbytes_wav)
            print(f"Total probabilidad: {sum(probabilidades_wav)}")
            f.close()
        print("ARCHIVO MP3")
        with ruta_limpia_mp3.open("rb") as f:
            #Inciso C, creo 256 contadores que son los posibles bytes y los inicializo en 0
            contadores_mp3 = [0] * 256
            #con un for recorro todo el archivo contando cuantas veces aparece cada byte en el archivo.
            datos_mp3 = f.read()
            for byte in datos_mp3:
                contadores_mp3[byte] += 1
            
            totalbytes_mp3 = sum(contadores_mp3) #cuento el tamaño total del archivo en bytes.
            print(f"Tamaño archivo mp3: {totalbytes_mp3}")
            probabilidades_mp3 = []
            for i in range(len(contadores_mp3)):
                print(f"Probabilidad del byte: {i}, {contadores_mp3[i]/totalbytes_mp3}")
                probabilidades_mp3.append(contadores_mp3[i]/totalbytes_mp3)
            print(f"Total probabilidad: {sum(probabilidades_mp3)}")

    valores_bytes = range(256)

    # Creamos el gráfico de barras
    plt.bar(valores_bytes, probabilidades_wav, width=1.0, color='blue')
    plt.title("Distribución de Probabilidades - Archivo WAV")
    plt.xlabel("Valor del Byte (0 - 255)")
    plt.ylabel("Probabilidad (Pi)")
    plt.show()

    plt.bar(valores_bytes, probabilidades_mp3, width=1.0, color='red')
    plt.title("Distribución de Probabilidades - Archivo MP3")
    plt.xlabel("Valor del Byte (0 - 255)")
    plt.ylabel("Probabilidad (Pi)")
    plt.show()
    print(f"ENTROPIA DEL ARCHIVO MP3: {calcular_entropia(probabilidades_mp3)}")
    print(f"ENTROPIA DEL ARCHIVO WAV: {calcular_entropia(probabilidades_wav)}")