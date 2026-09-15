import unicodedata

def distancia_hamming(cad1,cad2): #CALCULA LA DISTANCIA DE HAMMING ENTRE 2 CADENAS DE IGUAL LONGITUD. HACEMOS LANZAR UN ValueError si las longitudes son distintas
    if len(cad1) != len(cad2):
        raise ValueError("La Distancia de Hamming requiere que las cadenas tengan exactamente la misma longitud \n")
    
    distancia = sum(c1 != c2 for c1, c2 in zip(cad1,cad2)) #"zip" EMPAREJA LAS LETRAS QUE ESTAN EN EL MISMO INDICE 
    return distancia

def distancia_leveshtein(cad1,cad2): #CALCULA LA DISTANCIA DE LEVENSHTEIN (distancia de edicion) ENTRE DOS CADENAS.
                                    #PERMITE INSERCIONES, ELIMINACIONES Y SUSTITUCIONES 
    m = len(cad1)
    n = len(cad2)
    
    #SE CREA LA MATRIZ DE DISTANCIAS
    matriz_dist = [[0]*(n+1) for _ in range(m+1)]

    #INICIALIZAMOS LOS CASOS BASE (transformar cadena vacia)
    for i in range(m + 1):
        matriz_dist[i][0] = i
    for j in range(n + 1):
        matriz_dist[0][j] = j

    #LLENAMOS LA MATRIZ POR PROGRAMACION DINAMICA
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if cad1[i - 1] == cad2[j - 1]:
                costo = 0
            else:
                costo = 1
            matriz_dist[i][j] = min(
                matriz_dist[i-1][j] + 1,        #ELIMINACION
                matriz_dist[i][j-1] + 1,        #INSERCION
                matriz_dist[i-1][j-1] + costo)   #SUSTITUCION
    return matriz_dist[m][n]

def normalizar_texto(texto): 
    """LA HEURISTICA DE NORMALIZACION:
            - CONVIERTE A MINUSCULAS
            - ELIMINA TILDES y DIERESIS COMUNES
            - ELIMINA ESPACIOS EN BLANCO SOBRANTES AL INICIO, FINAL y DOBLES ESPACIOS"""
    
    #CONVERTIR A MINUSCULAS Y QUITAR ESPACIOS EXTRA
    texto_limpio = " ".join(texto.lower().split())
    #DESPONEMOS CARACTERES CON ACENTOS (NFD) y FILTRAMOS DIACRITICOS
    texto_normalizado = "".join(
        c for c in unicodedata.normalize('NFD', texto_limpio)
        if unicodedata.category(c) != 'Mn'
    )
    return texto_normalizado

def similitud_heuristica(cad1, cad2):
    """COMPARA 2 TEXTOS APLICANDO LA NORMALIZACION PREVIA Y CALCULANDO
    UN PORCENTAJE DE SIMILITUD BASADO EN LA DISTANCIA DE LEVESHTEIN"""

    c1_norm = normalizar_texto(cad1)
    c2_norm = normalizar_texto(cad2)
    if not c1_norm and not c2_norm:
        return 100.0
    dist = distancia_leveshtein(c1_norm, c2_norm)
    longitud_maxima = max(len(c1_norm), len(c2_norm))
    porcentaje = (1 - dist / longitud_maxima) * 100
    return dist, porcentaje

if __name__ == "__main__":
    print("=" * 60)
    print("EJERCICIO 6: MEDICION DE DISTANCIA ENTRE CADENAS - GRUPO 8: BRAVO, CATTANEO, NEHIN, QUIROGA")
    print("=" * 60)

    #a) Implementar una función que calcule la "Distancia de Hamming" entre dos cadenas. 
    # Demostrar con un ejemplo de ejecución por qué este algoritmo no es aplicable si las 
    # cadenas sufren desfases o tienen distinta longitud (ej. "Juan Perez" vs "Jaun Perez").
    print("\n[a] Demostracion de la limitacion de la Distancia de Hamming: ")
    c1 = "Juan Perez"
    c2 = "Jaun Perez"
    print(f"C1: '{c1}'")
    print(f"C2: '{c2}'")

    #TIENEN LA MISMA LONGITUD, POR LO QUE HAMMING SE PUEDE CALCULAR
    try:
        dist_h = distancia_hamming(c1,c2)
        print(f"--> Distancia de Hamming calculada: {dist_h}")
        print(" Se puede observar como un solo traspaso ('u' y 'a' intercambiados en 'Jaun') genera una distancia de 2,")
        print(" ya que Hamming evalua de forma estrictamente posicional sin entender inserciones/eliminaciones.")
    except Exception as e:
        print(f"--> ERROR EN HAMMING: {e}")

    c3 = "Juan"
    print(f"\nIntentando Hamming con longitudes diferentes ('{c1}' [l={len(c1)}] vs '{c3}' [l={len(c3)}]):")
    try:
        distancia_hamming(c1,c3)
    except ValueError as e:
        print(f"--> [FALLO ESPERADO] ValueError: {e}")
        print(" HAMMING NO PUEDE OPERAR SI HAY UNA DIFERENCIA DE LONGITUD (un caracter extra o faltante)")

    # b) y c) PRUEBAS CON LEVESHTEIN Y NOMBRES MAL TIPEADOS
    print("\n" + "-" * 50)
    print("[b y c] Pruebas de Leveshtein con nombres mal tipeados: ")
    parejas = [
        ("Horacio López", "Oracio López"),
        ("Juan Perez", "Jaun Perez"),
        ("María Sol", "Maria Sol"),
        ("Alejandro", "Alexander")
    ]

    for nom1, nom2 in parejas:
        dist_lev = distancia_leveshtein(nom1,nom2)
        print(f"--> Comparando '{nom1}' vs '{nom2}':")
        print(f" Distancia de Levenshtein: {dist_lev} operaciones de edicion.")

    # d) Heuristica propuesta
    print("\n" + "-" * 50)
    print("[d] Aplicacion de Heuristica de Comparacion (Normalizacion + Levenshtein):")
    for nom1, nom2 in parejas:
        c1_norm = normalizar_texto(nom1)
        c2_norm = normalizar_texto(nom2)
        dist_norm, sim = similitud_heuristica(nom1, nom2)
        print(f"--> Originales: '{nom1}' vs '{nom2}'")
        print(f"    Normalizados: '{c1_norm}' vs '{c2_norm}'")
        print(f"    Distancia Levenshtein normalizada: {dist_norm}")
        print(f"    Similitud porcentual: {sim:.2f}%")
        print()