

**Detección de Errores: Códigos de Control (Checksum) — CUIT/CUIL**

Materia: Teoría de Información
Carrera: Licenciatura en Ciencias de la Computación
Año: 2026

## Descripción

El sistema de identificación tributaria en Argentina (CUIT/CUIL) utiliza un **dígito verificador** para detectar alteraciones o errores de tipeo comunes, basándose en el **algoritmo de Módulo 11**. Este ejercicio implementa dicho algoritmo como un ejemplo concreto de **Código de Detección de Errores** aplicado en un sistema real.

El programa `Ejercicio7.py`:

1. **Solicita al usuario** un número de CUIT/CUIL completo de 11 dígitos.
2. **Valida el formato** de la entrada: que contenga exactamente 11 caracteres y que todos sean dígitos numéricos.
3. **Separa** los primeros 10 dígitos (identificador base) del undécimo dígito (dígito verificador ingresado por el usuario).
4. **Aplica el algoritmo de Módulo 11** sobre los primeros 10 dígitos para calcular cuál debería ser el dígito de control esperado.
5. **Compara** el dígito calculado con el dígito 11 ingresado e informa por pantalla si el CUIT/CUIL es **"Válido"** o **"Inválido"**.

## Lógica del algoritmo (Módulo 11)

1. Se multiplica cada uno de los primeros 10 dígitos por una secuencia fija de coeficientes:

   ```
   secuencia = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]
   ```

2. Se suman todos los productos obtenidos.
3. Se calcula el resto de dividir esa suma por 11 (`resto = suma % 11`).
4. El dígito verificador esperado se obtiene según el valor del resto:
   - Si `resto == 0` → dígito verificador = **0**
   - Si `resto == 1` → **no existe** un dígito verificador válido (0-9) para esa combinación; por lo tanto ese número no puede corresponder a un CUIT/CUIL real.
   - En cualquier otro caso → dígito verificador = `11 - resto`
5. Si el dígito verificador calculado coincide con el 11.º dígito ingresado por el usuario, el CUIT/CUIL es válido; caso contrario, es inválido.

## Requisitos

- Python 3.x (no requiere librerías externas)

## Uso

Ejecutar el script desde la terminal:

```bash
python Ejercicio7.py
```

El programa solicitará interactivamente el número de CUIT/CUIL:

```
Ingrese su numero de cuit (11 digitos, sin guiones): 20123456786
```

> **Nota:** El número debe ingresarse **sin guiones ni espacios**, como una cadena continua de 11 dígitos (por ejemplo: `20123456786`, no `20-12345678-6`).

### Salida esperada

Por consola se imprime:

- Los dígitos del CUIT/CUIL ingresado, separados en una lista.
- El dígito verificador calculado por el algoritmo de Módulo 11.
- El resultado final: **"El cuit ingresado es valido"** o **"El cuit ingresado es invalido"**.

Ejemplo de ejecución:

```
Ingrese su numero de cuit (11 digitos, sin guiones): 20123456786
Cuit ingresado:  [2, 0, 1, 2, 3, 4, 5, 6, 7, 8, 6]
Digito verificador calculado:  6
El cuit ingresado es valido
```

## Estructura del código

| Función | Descripción |
|---|---|
| `verificacion_formato(xcuit)` | Valida que la entrada tenga exactamente 11 caracteres y que todos sean dígitos numéricos. |
| `calcular_digito_verificador(lista_cuit)` | Aplica el algoritmo de Módulo 11 sobre los primeros 10 dígitos y devuelve el dígito verificador esperado (o `None` si la combinación no admite un dígito válido). |
| `verifica_numero_cuit(xcuit)` | Orquesta la validación completa: separa los dígitos, calcula el verificador esperado y lo compara contra el dígito ingresado por el usuario. |
| Bloque `__main__` | Solicita el CUIT/CUIL por teclado y ejecuta la validación de formato y de dígito verificador. |

## Interpretación de resultados

El dígito verificador del CUIT/CUIL funciona como un **código de detección de errores sistemático**: permite detectar la gran mayoría de los errores de tipeo comunes (dígitos cambiados, transpuestos, etc.) sin necesidad de una base de datos externa, ya que la validez del número puede verificarse matemáticamente a partir de sus propios dígitos. Esto es análogo a otros mecanismos de control como el dígito verificador de tarjetas de crédito (algoritmo de Luhn) o el bit de paridad en transmisión de datos: en todos los casos se agrega **redundancia controlada** a la información para poder detectar (y en algunos casos corregir) errores introducidos durante su transcripción o transmisión.
