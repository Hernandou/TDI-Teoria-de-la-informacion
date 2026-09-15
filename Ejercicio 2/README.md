# Ejercicio 2: Análisis de Entropía y Compresión en Imágenes (BMP vs. JPG)

## ¿De qué trata?
Analiza y compara el contenido de información y la **Entropía de Shannon** entre una imagen sin compresión (**BMP**) y una imagen comprimida con pérdida (**JPG**):

1. **Lectura de Cabecera BMP:** Extrae metadatos binarios mediante `struct` (firma `'BM'`, dimensiones ancho $\times$ alto, profundidad de color en bits y tamaño).
2. **Distribución de Probabilidad de Bytes:** Cuenta la frecuencia de cada valor de byte ($0$ a $255$) en ambos archivos y calcula su probabilidad $P(x)$.
3. **Cálculo de Entropía de Shannon:**
   $$H = -\sum_{i=0}^{255} P(x_i) \cdot \log_2(P(x_i)) \quad [\text{bits/byte}]$$
   - **BMP:** Presenta redundancia y picos en ciertos valores, resultando en menor entropía y mayor tamaño en disco.
   - **JPG:** Al aplicar compresión (DCT y codificación entrópica), la distribución de los bytes se homogeniza, acercando la entropía al máximo teórico ($8\text{ bits/byte}$) con un tamaño mucho menor.
4. **Visualización:** Genera dos gráficos de barras comparativos con `matplotlib` mostrando la distribución de frecuencias de los bytes ($0 - 255$).

---

## Requisitos
- **Python 3.10 o superior**.
- **Librería externa:** Requiere `matplotlib`.
  ```powershell
  pip install matplotlib
  ```

---

## Cómo ejecutarlo
Desde la terminal en la raíz del proyecto:
```powershell
python "Ejercicio 2/Ejercicio2.py"
```

El script solicitará las rutas de los archivos a comparar (podés usar los ejemplos incluidos en la carpeta):
- **Ruta BMP:** `Ejercicio 2/EjemploBMP.bmp`
- **Ruta JPG:** `Ejercicio 2/EjemploJPG.jpg`
