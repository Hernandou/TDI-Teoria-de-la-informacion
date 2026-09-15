def verificacion_formato(xcuit):
    """Valida que la entrada tenga exactamente 11 dígitos numéricos."""
    if not xcuit.isdigit():
        print("Error: el CUIT/CUIL debe contener solo dígitos numéricos.")
        return False
    if len(xcuit) != 11:
        print(f"Error: el CUIT/CUIL debe tener 11 dígitos. Ingresaste {len(xcuit)}.")
        return False
    return True


def calcular_digito_verificador(lista_cuit):
    """Calcula el dígito verificador esperado (Módulo 11) a partir
    de los primeros 10 dígitos del CUIT/CUIL."""
    secuencia = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]
    primeros_diez = lista_cuit[:10]

    multip = [a * b for a, b in zip(secuencia, primeros_diez)]
    sumatoria = sum(multip)
    resto = sumatoria % 11

    if resto == 0:
        digito_z = 0
    elif resto == 1:
        # Con resto = 1 no existe un dígito verificador válido (0-9),
        # por lo tanto ningún CUIT puede terminar cumpliendo esta condición.
        digito_z = None
    else:
        digito_z = 11 - resto

    return digito_z


def verifica_numero_cuit(xcuit):
    cuit = int(xcuit)
    lista_cuit = [int(digito) for digito in str(cuit).zfill(11)]
    print("Cuit ingresado: ", lista_cuit)

    digito_z = calcular_digito_verificador(lista_cuit)
    print("Digito verificador calculado: ", digito_z)

    if digito_z is None:
        print("El cuit ingresado es invalido (no existe un digito verificador posible para este calculo).")
        return False

    digito_ingresado = lista_cuit[10]
    if digito_z == digito_ingresado:
        print("El cuit ingresado es valido")
        return True
    else:
        print("El cuit ingresado es invalido")
        return False


if __name__ == "__main__":
    cuit_ingresado = input("Ingrese su numero de cuit (11 digitos, sin guiones): ").strip()

    if verificacion_formato(cuit_ingresado):
        verifica_numero_cuit(cuit_ingresado)