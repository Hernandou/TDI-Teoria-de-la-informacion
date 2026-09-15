import math
import struct
from pathlib import Path
import matplotlib.pyplot as plt


def calcular_entropia(lista_probabilidades):
    entropia = 0.0
    for p in lista_probabilidades:
        if p > 0:
            entropia -= p * math.log2(p)
    return entropia


def verificacion_archivo(xruta, xtipo):
    if not xruta.exists():
        print(f"Error: La ruta '{xruta}' no existe.")
        return False
    if not xruta.is_file():
        print(f"Error: La ruta '{xruta}' no corresponde a un archivo.")
        return False

    ext = xruta.suffix.lower()
    if xtipo == "bmp" and ext not in [".bmp"]:
        print(f"El archivo es {ext}. Se esperaba .bmp")
        return False
    elif xtipo == "jpg" and ext not in [".jpg", ".jpeg"]:
        print(f"El archivo es {ext}. Se esperaba .jpg o .jpeg")
        return False

    print(f"Archivo {xtipo.upper()} cargado correctamente.")
    return True


def calcular_probabilidades(ruta_archivo):

    contadores = [0] * 256
    with ruta_archivo.open("rb") as f:
        datos = f.read()

    total_bytes = len(datos)
    for byte in datos:
        contadores[byte] += 1

    probabilidades = []
    for count in contadores:
        p = count / total_bytes
        print(f"Probabilidad del byte {len(probabilidades)}: {p}")
        probabilidades.append(p)
    return probabilidades, total_bytes


if __name__ == "__main__":
    entrada_bmp = input("Ingresa la ruta del archivo BMP: ")
    entrada_jpg = input("Ingresa la ruta del archivo JPG: ")

    ruta_bmp = Path(entrada_bmp.strip("\"'"))
    ruta_jpg = Path(entrada_jpg.strip("\"'"))

    if verificacion_archivo(ruta_bmp, "bmp") and verificacion_archivo(
        ruta_jpg, "jpg"
    ):

        # --- ANÁLISIS DE CABECERA BMP ---
        print("\n--- ANÁLISIS DEL ARCHIVO BMP ---")
        with ruta_bmp.open("rb") as f:
            cabecera = f.read(54)
            # Los primeros 2 bytes indican la firma ("BM")
            firma = cabecera[0:2].decode("ascii", errors="ignore")
            if firma == "BM":
                print("Firma BMP válida ('BM')")
            else:
                print("Advertencia: No parece un archivo BMP estándar.")

            tamano_archivo = struct.unpack("<I", cabecera[2:6])[0]
            ancho = struct.unpack("<i", cabecera[18:22])[0]
            alto = struct.unpack("<i", cabecera[22:26])[0]
            bpp = struct.unpack("<H", cabecera[28:30])[0]

            print(f"Dimensiones: {ancho} x {alto} píxeles")
            print(f"Profundidad de color: {bpp} bits por píxel")
            print(f"Tamaño reportado en cabecera: {tamano_archivo} bytes")

        # --- CÁLCULO DE PROBABILIDADES Y ENTROPÍA ---
        print("\n-- PROBABILIDADES DEL ARCHIVO BMP --")
        prob_bmp, total_bmp = calcular_probabilidades(ruta_bmp)
        print("\n-- PROBABILIDADES DEL ARCHIVO JPG --")
        prob_jpg, total_jpg = calcular_probabilidades(ruta_jpg)

        print(f"\nTamaño real BMP: {total_bmp} bytes")
        print(f"Tamaño real JPG: {total_jpg} bytes")

        entropia_bmp = calcular_entropia(prob_bmp)
        entropia_jpg = calcular_entropia(prob_jpg)

        print(f"\nENTROPÍA DEL ARCHIVO BMP: {entropia_bmp:.4f} bits/byte")
        print(f"ENTROPÍA DEL ARCHIVO JPG: {entropia_jpg:.4f} bits/byte")

        # --- GRAFICACIÓN ---
        valores_bytes = range(256)

        plt.figure(figsize=(12, 5))

        # Gráfico BMP
        plt.subplot(1, 2, 1)
        plt.bar(valores_bytes, prob_bmp, width=1.0, color="blue")
        plt.title("Distribución de Bytes - BMP (Sin Compresión)")
        plt.xlabel("Valor del Byte (0 - 255)")
        plt.ylabel("Probabilidad (Pi)")

        # Gráfico JPG
        plt.subplot(1, 2, 2)
        plt.bar(valores_bytes, prob_jpg, width=1.0, color="red")
        plt.title("Distribución de Bytes - JPG (Comprimido)")
        plt.xlabel("Valor del Byte (0 - 255)")
        plt.ylabel("Probabilidad (Pi)")

        plt.tight_layout()
        plt.show()