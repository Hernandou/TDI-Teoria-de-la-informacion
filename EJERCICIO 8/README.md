# Teoría de la Información - Práctico de Máquina N° 1
## Ejercicio 8: Cálculo de Capacidad de Canal por Búsqueda Exhaustiva (Canal 2x4)

Este repositorio contiene la solución implementada en Python para el **Ejercicio 8** del primer práctico de máquina de la asignatura **Teoría de la Información** (Licenciatura en Ciencias de la Computación).

---

## 📌 Descripción del Proyecto

El objetivo de este programa es determinar de manera numérica la **Capacidad de Canal (C)** para un canal discreto sin memoria con alfabeto de entrada binario (X = {0, 1}) y alfabeto de salida cuaternario (Y = {0, 1, 2, 3}), definido por una matriz de probabilidades de transición `P(Y|X)` de dimensión `2x4` (`P(Y_j | X_i)`).

Dado que la Capacidad de Canal se define como el máximo de la **Información Mutua** `I(X;Y)` sobre todas las posibles distribuciones de entrada `P(X)`:

```text
C = max(I(X;Y))
```

El script utiliza un algoritmo de **búsqueda exhaustiva** variando la probabilidad de entrada `P(X=0)` de 0.00 a 1.00 en incrementos del paso configurable (`paso = 0.01`), evaluando `I(X;Y)` en cada iteración hasta hallar el valor máximo (`capacidad_max`) y la distribución óptima de entrada (`p_x_optima`).

---

## 📐 Fundamento Teórico y Estructura del Código

El cálculo implementado en la función `calcular_capacidad_exhaustiva()` reproduce las siguientes etapas de Teoría de la Información de forma fiel al script:

1. **Cálculo de la Entropía de Shannon (`calcular_entropia_vector`)**:
   Para un vector de probabilidades, calcula la entropía ignorando cualquier probabilidad menor o igual a 1e-9 para evitar problemas con 0 en log2:
   ```text
   entropia -= p * math.log2(p)  (para cada p > 1e-9)
   ```

2. **1° Probabilidades de Salida P(Y_j) usando el Teorema de la Probabilidad Total**:
   ```text
   P(Y_j) = P(X=0) * P(Y_j | X=0) + P(X=1) * P(Y_j | X=1)
   ```
   Calculado para cada salida j de 0 a 3:
   ```python
   P_Y[j] = P_X[0] * matriz_canal[0][j] + P_X[1] * matriz_canal[1][j]
   ```

3. **2° Entropía de la Salida H(Y)**:
   ```python
   H_Y = calcular_entropia_vector(P_Y)
   ```

4. **3° Entropía Condicional H(Y|X) (Ruido del Canal)**:
   ```text
   H(Y|X) = P(X=0) * H(Y|X=0) + P(X=1) * H(Y|X=1)
   ```
   En el código se calcula la entropía de cada fila de la matriz y luego su promedio ponderado:
   ```python
   H_Y_dado_X0 = calcular_entropia_vector(matriz_canal[0])
   H_Y_dado_X1 = calcular_entropia_vector(matriz_canal[1])
   H_Y_dado_X = P_X[0] * H_Y_dado_X0 + P_X[1] * H_Y_dado_X1
   ```

5. **4° Información Mutua I(X;Y)**:
   ```python
   I_XY = H_Y - H_Y_dado_X
   ```

A lo largo del barrido se compara y almacena el valor máximo:
```python
if I_XY > capacidad_max:
    capacidad_max = I_XY
    p_x_optima = P_X
```

---

## 💻 Características del Código

- **Modo Demostración**: Incluye una matriz de transición de `2x4` por defecto para verificar el correcto funcionamiento del algoritmo:
  - Fila X = 0: `[0.4, 0.3, 0.2, 0.1]`
  - Fila X = 1: `[0.1, 0.2, 0.3, 0.4]`
- **Modo Interactivo (`ingresar_matriz_manual`)**: Permite al usuario ingresar por consola una matriz personalizada de `2x4`.
- **Validación Rigurosa**:
  - Verifica que se ingresen exactamente 4 valores por fila.
  - Comprueba que la suma de probabilidades de cada fila sea estrictamente igual a 1.0 (validado con tolerancia de punto flotante `math.isclose(suma, 1.0, abs_tol=1e-5)`).
  - Maneja casos numéricos evitando errores con `math.log2(0)` mediante filtrado de probabilidades nulas (`p > 1e-9`).
- **Sin dependencias externas**: Implementado puramente en Python utilizando únicamente el módulo nativo `math`.

---

## 🚀 Requisitos e Instalación

### Requisitos Prerequisito
- **Python 3.7+** (no se requieren librerías de terceros como NumPy o SciPy).

### Ejecución
1. Clonar o descargar este repositorio:
   ```bash
   git clone https://github.com/Hernandou/TDI-Teoria-de-la-informacion
   cd TDI-Teoria-de-la-informacion
   ```

2. Ejecutar el script principal:
   ```bash
   python ejercicio8.py
   # O en Windows:
   py ejercicio8.py
   ```

---

## 🖥️ Ejemplo de Uso y Salida

Al ejecutar el programa, se calcula primero la capacidad para la matriz por defecto:

```text
=================================================================
EJERCICIO 8: CALCULO DE CAPACIDAD DE CANAL POR BUSQUEDA EXHAUSTIVA (2x4) --- GRUPO 8: BRAVO, CATTANEO, NEHIN, QUIROGA
=================================================================

 Matriz de Transicion P(Y|X) utilizada por defecto para demostracion:
  X = 0 -> Y: [0.4, 0.3, 0.2, 0.1]
  X = 1 -> Y: [0.1, 0.2, 0.3, 0.4]

----RESULTADOS DEL BARRIDO EXHAUSTIVO (Paso=0.01)----
--> CAPACIDAD DEL CANAL (C): 0.153561 bits/simbolo
--> DISTRIBUCION DE ENTRADA OPTIMA:
    P(X=0) = 0.50
    P(X=1) = 0.50

--------------------------------------------------
¿Desea ingresar una matriz personalizada de 2x4 manualmente por teclado? (s/n)
```

Si el usuario responde `s`, podrá ingresar una nueva matriz fila por fila introduciendo los 4 valores separados por espacio.

---

## 👥 Integrantes - Grupo 8

- **Bravo**
- **Cattaneo**
- **Nehin**
- **Quiroga**

*Carrera: Licenciatura en Ciencias de la Computación*  
*Materia: Teoría de la Información*
