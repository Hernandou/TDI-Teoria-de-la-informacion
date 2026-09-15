import math

def calcular_entropia_vector(prob_vector):
    """ CALCULAMOS LA ENTROPIA DE SHANNON PARA UN VECTOR DE PROBABILIDADES
    SE IGNORA CUALQUIER VALOR DDE PROBABILIDAD IGUAL A 0"""
    entropia = 0.0
    for p in prob_vector:
        if p > 1e-9: #EVITAMOS PROBLEMAS DE PRECISION CON 0
            entropia -= p * math.log2(p)
    return entropia

def calcular_capacidad_exhaustiva(matriz_canal, paso = 0.01):
    """ DETERMINAMOS LA CAPACIDAD DE CANAL (C) MEDIANTE BUSQUEDA EXHAUSTIVA DE P(X) CON UN PASO DADO
    matriz_canal : lista de listas de 2x4 (P(Y_j | X_i))"""
    capacidad_max = -1.0
    p_x_optima = None
    historial_iteraciones = []

    #ITERAMOS P(X=0) de 0.00 a 1.00 EN INCREMENTOS DEL PASO
    num_pasos = int(round(1.0 / paso)) + 1
    for k in range(num_pasos):
        px0 = k * paso
        if px0 > 1.0:
            px0 = 1.0
        px1 = 1.0 - px0
        P_X = [px0, px1]

        #1° CALCULAMOS PROBABILIDADES DE SALIDA P(Y_j) USANDO TEOREMA DE LA PROBABILIDAD TOTAL:
        #P(Y_j) = P(X=0) * P(Y_j | X=0) + P(X=1) * P(Y_j | X=1)
        P_Y = [0.0] * 4
        for j in range (4):
            P_Y[j] = P_X[0] * matriz_canal[0][j] + P_X[1] * matriz_canal[1][j]

        #2° CALCULAMOS LA ENTROPIA DE LA SALIDA H(Y)
        H_Y = calcular_entropia_vector(P_Y)

        #3° CALCULAMOS LA ENTROPIA CONDICIONAL H(Y|X) (RUIDO DEL CANAL)
        # H(Y|X) = P(X=0) * H(Y|X=0) + P(X=1) * H(Y|X=1)
        H_Y_dado_X0 = calcular_entropia_vector(matriz_canal[0])
        H_Y_dado_X1 = calcular_entropia_vector(matriz_canal[1])
        H_Y_dado_X = P_X[0] * H_Y_dado_X0 + P_X[1] * H_Y_dado_X1

        #4° CALCULAMOS LA INFORMACION MUTUA I(X;Y)
        I_XY = H_Y - H_Y_dado_X

        #REGISTRAMOS PARA EL ANALISIS O DEBUGGING SI ES NECESARIO
        historial_iteraciones.append((P_X, P_Y, H_Y, H_Y_dado_X, I_XY))

        #GUARDAMOS EL MAXIMO
        if I_XY > capacidad_max:
            capacidad_max = I_XY
            p_x_optima = P_X

    return capacidad_max, p_x_optima, historial_iteraciones

def ingresar_matriz_manual():
    """SOLICITAMOS AL USUARIO LOS 8 VALORES DE LA MATRIZ DE TRANSICION DE 2x4
    Y VALIDAMOS QUE CADA FILA SUME ESTRICTAMENTE 1"""
    print("\n----Ingreso de la Matriz de Canal P(Y|X) de 2x4----")
    matriz = []
    for i in range(2):
        while True:
            try:
                entrada = input(f"Ingrese las 4 probabilidades para la fila X= {i} (¡¡SEPARADAS POR ESPACIO!!): ")
                valores = [float(x) for x in entrada.replace(',', '.').split()]
                if len(valores) != 4:
                    print(f"ERROR: DEBE INGRESAR EXACTAMENTE 4 VALORES. INGRESO {len(valores)}.")
                    continue
                #VALIDAMOS LA SUMA IGUAL A 1 CON TOLERANCIA POR PUNTO FLOTANTE
                suma = sum(valores)
                if not math.isclose(suma, 1.0, abs_tol= 1e-5):
                    print(f"ERROR: LA SUMA DE LA FILA DEBE SER ESTRICTAMENTE 1.0 (SU SUMA FUE: {suma:.5f}). REINTENTE")
                    continue
                matriz.append(valores)
                break
            except ValueError:
                print("ERROR: ¡INGRESE NUMEROS DECIMALES VALIDOS!")
    return matriz

if __name__ == "__main__":
    print("=" * 65)
    print("EJERCICIO 8: CALCULO DE CAPACIDAD DE CANAL POR BUSQUEDA EXHAUSTIVA (2x4) --- GRUPO 8: BRAVO, CATTANEO, NEHIN, QUIROGA")
    print("=" * 65)

    #MATRIZ PRO DEFECTO PARA DEMOSTRACION (canal binario a cuaternario no uniforme de ejemplo)
    #Fila X=0: [0.4, 0.3, 0.2, 0.1]
    #Fila X=1: [0.1, 0.2, 0.3, 0.4]
    matriz_x_defecto = [
        [0.4, 0.3, 0.2, 0.1],
        [0.1, 0.2, 0.3, 0.4]
    ]
    print("\n Matriz de Transicion P(Y|X) utilizada por defecto para demostracion:")
    for i, fila in enumerate(matriz_x_defecto):
        print(f"  X = {i} -> Y: {fila}")

    cap, px_opt, hist = calcular_capacidad_exhaustiva(matriz_x_defecto, paso=0.01)

    print(f"\n----RESULTADOS DEL BARRIDO EXHAUSTIVO (Paso=0.01)----")
    print(f"--> CAPACIDAD DEL CANAL (C): {cap:.6f} bits/simbolo")
    print(f"--> DISTRIBUCION DE ENTRADA OPTIMA:")
    print(f"    P(X=0) = {px_opt[0]:.2f}")
    print(f"    P(X=1) = {px_opt[1]:.2f}")

    #AQUI LE DAMOS LA OPORTUNIDAD AL USUARIO PARA INGRESAR SU MATRIZ
    print("\n" + "-" * 50)
    respuesta = input("¿Desea ingresar una matriz personalizada de 2x4 manualmente por teclado? (s/n)").strip().lower()
    if respuesta in ['s', 'si', 'y', 'yes']:
        matriz_usuario = ingresar_matriz_manual()
        cap_u, px_opt_u, _ = calcular_capacidad_exhaustiva(matriz_usuario, paso=0.01)
        print("\n" + "=" * 50)
        print("-----RESULTADOS DE SU MATRIZ PERSONALIZADA-----")
        print(f"--> CAPACIDAD DEL CANAL (C): {cap_u:.6f} bits/simbolo")
        print(f"--> DISTRIBUCION DE ENTRADA OPTIMA:")
        print(f"    P(X=0) = {px_opt_u[0]:.2f}")
        print(f"    P(X=1) = {px_opt_u[1]:.2f}")
        print("=" * 50)
    else:
        print("\nOPERACION FINALIZADA SIN INGRESO MANUAL")
       