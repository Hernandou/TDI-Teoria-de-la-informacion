
from pathlib import Path
import math
from collections import Counter



def calcular_entropia(lista_probabilidades):
    entropia = 0.0
    for p in lista_probabilidades:
        if p > 0:  # Evitamos el error matemático de log2(0)
            entropia -= p * math.log2(p)
    return entropia
def calcular_redundancia(xentropia):
    #calculamos la entropia maxima de un archivo binario
    entropia_max = math.log2(256)
    return entropia_max - xentropia
def verificacion_archivo(xruta):

        if not xruta.exists():
            print("La ruta seleccionada no existe.")
            return False
        elif not xruta.is_file():
            print("La ruta no corresponde a un archivo, podria ser un directorio.")
            return False
        else:
            print("Archivo cargado correctamente")
            return True
        
if __name__ == "__main__":
    #Solicitamos las rutas del archivo
    entrada_1 = input("Ingresa la ruta del archivo 1: ")

    ruta_1 = entrada_1.strip("\"'")

    ruta_limpia_1 = Path(ruta_1)

    if verificacion_archivo(ruta_limpia_1):
        print("ANALISIS DEL ARCHIVO 1")
        with ruta_limpia_1.open("rb") as f:
            #Inciso C, creo 256 contadores que son los posibles bytes y los inicializo en 0
            contadores_1 = [0] * 256
            #con un for recorro todo el archivo contando cuantas veces aparece cada byte en el archivo.
            datos_1 = f.read()
            for byte in datos_1:
                contadores_1[byte] += 1
            totalbytes_1 = sum(contadores_1) #cuento el tamaño total del archivo en bytes.
            print(f"Tamaño archivo 1: {totalbytes_1}")
            probabilidades_1 = []
            for i in range(len(contadores_1)):
                print(f"Probabilidad del byte: {i}, {contadores_1[i]/totalbytes_1}")
                probabilidades_1.append(contadores_1[i]/totalbytes_1)
            print(f"Total probabilidad: {sum(probabilidades_1)}")
            entropia_1 = calcular_entropia(probabilidades_1)
            redundancia_1 = calcular_redundancia(entropia_1)
            print(f"ENTROPIA DEL ARCHIVO 1: {entropia_1}")
            print(f"REDUNDANCIA DEL ARCHIVO 1: {redundancia_1}")
            f.close()
            
    
