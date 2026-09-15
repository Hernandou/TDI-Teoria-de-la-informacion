# Práctico de Máquina 1 — Ejercicio 1

**Análisis de Información en Señales de Audio (Formato WAV vs. MP3)**

## Descripción

El formato WAV sin compresión (PCM) almacena las muestras de audio de forma secuencial, mientras que el formato MP3 aplica compresión con pérdida. El objetivo de este ejercicio es **analizar la cantidad de información real que transporta una señal de audio**, comparando un archivo `.wav` y un archivo `.mp3` que contengan exactamente la misma pista de audio.

El programa `Ejercicio1.py`:

1. **Carga y validación** de los archivos de entrada, verificando que las extensiones y formatos correspondan efectivamente a WAV y MP3.
2. **Análisis de cabecera** del archivo WAV: lee y aísla la cabecera RIFF/WAVE (44 bytes) e imprime en pantalla el identificador RIFF, el formato, el tamaño del archivo, la frecuencia de muestreo y el número de canales.
3. **Distribución de probabilidades**: lee ambos archivos byte por byte (valores de 0 a 255) y calcula la frecuencia relativa de aparición de cada símbolo, obteniendo así la distribución de probabilidad `p_i` de cada fuente.
4. **Histogramas**: genera un gráfico de barras con la distribución de probabilidades de cada archivo, permitiendo comparar visualmente ambas fuentes.
5. **Cálculo de entropía**: a partir de las probabilidades obtenidas, calcula la entropía empírica de Shannon para ambas fuentes:

   ```
   H = - Σ p_i · log2(p_i)
   ```

## Requisitos

- Python 3.x
- Librería `matplotlib`

Instalación de dependencias:

```bash
pip install matplotlib
```

## Uso

Ejecutar el script desde la terminal:

```bash
python Ejercicio1.py
```

El programa solicitará interactivamente las rutas de los archivos:

```
Ingresa la ruta del archivo mp3: /ruta/a/pista.mp3
Ingresa la ruta del archivo WAV: /ruta/a/pista.wav
```

> **Nota:** Las rutas pueden ingresarse con o sin comillas; el programa las limpia automáticamente. Se recomienda usar un archivo `.wav` y un archivo `.mp3` que contengan **exactamente la misma pista de audio** para que la comparación sea válida.

### Salida esperada

Por consola se imprime:

- Validación de los archivos cargados (extensión/tipo correcto).
- **Análisis de cabecera WAV**: chunk ID, formato, tamaño del archivo, frecuencia de muestreo y número de canales.
- Tabla de probabilidad de aparición para cada uno de los 256 valores de byte (0–255), tanto del WAV como del MP3, junto con la verificación de que la suma total de probabilidades sea 1.
- Dos gráficos (uno por archivo) mostrando el histograma de probabilidades por valor de byte.
- **Entropía calculada** para el archivo MP3 y para el archivo WAV, expresada en bits/símbolo.

## Estructura del código

| Función | Descripción |
|---|---|
| `calcular_entropia(lista_probabilidades)` | Aplica la fórmula de Shannon sobre una lista de probabilidades, evitando el error de `log2(0)`. |
| `verificacion_archivo(xruta, xtipo)` | Valida que la ruta exista, sea un archivo y tenga la extensión esperada (`.wav` o `.mp3`). |
| Bloque `__main__` | Orquesta la carga de archivos, el análisis de cabecera, el cálculo de distribuciones de probabilidad, la generación de histogramas y el cálculo final de entropía. |

## Interpretación de resultados

Se espera que:

- El archivo **WAV** (sin compresión) muestre una distribución de bytes con **picos y patrones**, reflejo de la redundancia presente en la señal PCM, y por lo tanto una **entropía menor** al máximo teórico de 8 bits/símbolo.
- El archivo **MP3** (comprimido) muestre una distribución de bytes **más uniforme**, dado que la compresión elimina gran parte de la redundancia, acercando su entropía empírica al límite teórico de **8 bits/símbolo**.

Esta diferencia ilustra el principio central de la Teoría de la Información: la compresión reduce la redundancia de la fuente, acercando la entropía empírica de los datos a su máximo posible.

