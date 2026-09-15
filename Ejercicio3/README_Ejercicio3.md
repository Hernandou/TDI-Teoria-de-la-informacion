# Práctico de Máquina 1 — Ejercicio 3

**Entropía Empírica en Archivos (Texto vs. Comprimidos)**

Materia: Teoría de Información
Carrera: Licenciatura en Ciencias de la Computación
Año: 2026

## Descripción

El objetivo de este ejercicio es desarrollar una aplicación que lea un archivo arbitrario **byte por byte** (en tiempo O(N), siendo N el tamaño del archivo) y calcule su **entropía empírica** y su **redundancia**, para luego comparar los resultados entre un archivo de texto plano y un archivo fuertemente comprimido.

El programa `Ejercicio3.py`:

1. **Carga y validación** del archivo de entrada, verificando que la ruta exista y corresponda efectivamente a un archivo (no un directorio).
2. **Distribución de probabilidades**: lee el archivo byte por byte (valores de 0 a 255) y calcula la frecuencia relativa de aparición de cada símbolo, obteniendo la distribución de probabilidad `p_i` de la fuente.
3. **Cálculo de entropía empírica**, aplicando la fórmula de Shannon:

   ```
   H = - Σ p_i · log2(p_i)
   ```

4. **Cálculo de redundancia**, como la diferencia entre la entropía máxima teórica de una fuente de 256 símbolos (8 bits/símbolo) y la entropía empírica real obtenida:

   ```
   R = H_max - H = log2(256) - H
   ```

## Requisitos

- Python 3.x (no requiere librerías externas)

## Uso

Ejecutar el script desde la terminal:

```bash
python Ejercicio3.py
```

El programa solicitará interactivamente la ruta del archivo a analizar:

```
Ingresa la ruta del archivo 1: /ruta/a/archivo.txt
```

> **Nota:** La ruta puede ingresarse con o sin comillas; el programa las limpia automáticamente.

Según la consigna, el programa debe ejecutarse **dos veces** para poder comparar resultados:

1. Una vez utilizando como entrada un **archivo de texto puro** (`.txt`).
2. Otra vez utilizando como entrada un **archivo fuertemente comprimido** (`.zip` o `.rar`) de **tamaño similar** al anterior.

### Salida esperada

Por consola se imprime:

- Confirmación de que el archivo fue cargado correctamente.
- Tamaño total del archivo en bytes.
- Tabla de probabilidad de aparición para cada uno de los 256 valores de byte (0–255), junto con la verificación de que la suma total de probabilidades sea 1.
- **Entropía empírica** del archivo, expresada en bits/símbolo.
- **Redundancia** del archivo, expresada en bits/símbolo.

## Estructura del código

| Función | Descripción |
|---|---|
| `calcular_entropia(lista_probabilidades)` | Aplica la fórmula de Shannon sobre una lista de probabilidades, evitando el error de `log2(0)`. |
| `calcular_redundancia(xentropia)` | Calcula la redundancia como la diferencia entre la entropía máxima teórica de un archivo binario (`log2(256) = 8 bits`) y la entropía empírica calculada. |
| `verificacion_archivo(xruta)` | Valida que la ruta exista y sea un archivo (independientemente de su extensión). |
| Bloque `__main__` | Orquesta la carga del archivo, el cálculo de la distribución de probabilidades, y el cálculo final de entropía y redundancia. |

## Interpretación de resultados

- Un **archivo de texto plano** (`.txt`) presenta patrones repetitivos y una distribución de bytes desigual (ciertos caracteres, como espacios y letras comunes, aparecen con mucha más frecuencia que otros). Esto genera una **redundancia alta** y una **entropía empírica notablemente menor** al máximo teórico de 8 bits/símbolo.

- Un **archivo fuertemente comprimido** (`.zip` o `.rar`) ya tuvo su redundancia eliminada por el algoritmo de compresión, que suprime los patrones predecibles del archivo original. Como consecuencia, los 256 valores de byte tienden a distribuirse de manera casi uniforme, la incertidumbre de los datos se maximiza y la **entropía empírica se acerca al límite teórico de 8 bits/símbolo**, con una **redundancia cercana a cero**.

En síntesis: cuanto mejor es un algoritmo de compresión, más se acerca la entropía empírica del archivo resultante a su máximo teórico, ya que su objetivo es precisamente eliminar la redundancia (información predecible) presente en los datos originales.

