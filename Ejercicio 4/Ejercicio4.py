from pathlib import Path

def analizarIC(xtexto):
    print("Caracteres: ", xtexto)
    elementos = list(set(xtexto))
    terms = []
    for c in elementos:
        t = xtexto.count(c) * (xtexto.count(c) - 1)
        terms.append(t)
    s = sum(terms)
    tpdl = len(xtexto) * (len(xtexto) - 1)
    ic = s / tpdl
    return ic

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

if __name__ == '__main__':
    archivo = input("Ingrese ruta del archivo: ")
    ruta = archivo.strip("\"'")
    rutaL = Path(ruta)

    if verificacion_archivo(rutaL):
        print("ANÁLISIS DEL ARCHIVO: ")
        with rutaL.open('r') as f:
            texto = f.read()
            ic = analizarIC(list(texto))
        print(f"El Índice de Coincidencia del texto {texto} es de: {ic}")