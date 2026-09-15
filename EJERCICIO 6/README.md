# Medición de Distancia entre Cadenas (Hamming vs. Levenshtein)

Trabajo práctico para la materia **Teoría de la Información** de la **Licenciatura en Ciencias de la Computación** (4° año).

---

## 📌 ¿De qué trata este proyecto?

En tareas de procesamiento de lenguaje natural, motores de búsqueda o limpieza de bases de datos, es muy común toparse con nombres o palabras mal escritas, diferencias de acentuación o caracteres faltantes (por ejemplo: `"María Sol"` vs `"Maria Sol"` o `"Juan Perez"` vs `"Jaun Perez"`).

El objetivo de este proyecto es implementar, analizar y comparar algoritmos clásicos de medición de distancia entre cadenas de texto, demostrando en la práctica las limitaciones de unos frente a otros, y proponiendo una heurística para calcular un porcentaje de similitud más robusto frente a errores frecuentes.

---

## 👥 Integrantes (Grupo 8)

* **Bravo**
* **Cattaneo**
* **Nehin**
* **Quiroga**

---

## 🧠 Métricas y Conceptos Implementados

### 1. Distancia de Hamming
Mide el número de posiciones en las cuales los caracteres correspondientes de dos cadenas son diferentes.
* **Requisito estricto:** Ambas cadenas deben tener exactamente la misma longitud. Si difieren, la función arroja un error (`ValueError`).
* **Limitación demostrada:** Al evaluar posición por posición, no tolera desfasajes ni transposiciones simples. Por ejemplo, al comparar `"Juan Perez"` con `"Jaun Perez"`, la distancia calculada es `2` (falla en `'u'` vs `'a'` y en `'a'` vs `'u'`), cuando en realidad solo hubo un traspaso de lugar entre dos letras adyacentes.

### 2. Distancia de Levenshtein (Distancia de Edición)
Calcula el número mínimo de operaciones elementales requeridas para transformar una cadena en otra. Las operaciones admitidas son:
* **Inserción** de un carácter.
* **Eliminación** de un carácter.
* **Sustitución** de un carácter por otro.

Se resuelve mediante **programación dinámica** construyendo una matriz donde cada celda acumula el costo óptimo de transformar los prefijos de ambas cadenas. A diferencia de Hamming, soporta cadenas de diferente longitud y desfases causados por letras agregadas o quitadas.

### 3. Heurística de Normalización y Similitud Porcentual
Para comparar nombres reales de manera justa, se diseñó una etapa de preprocesamiento antes de medir la distancia:
1. **Conversión a minúsculas:** Evita penalizar diferencias de mayúsculas/minúsculas.
2. **Limpieza de espacios en blanco:** Quita espacios al inicio, al final y reduce espacios intermedios duplicados.
3. **Normalización Unicode (NFD):** Descompone caracteres acentuados y filtra marcas diacríticas (`á` $\to$ `a`, `ü` $\to$ `u`, etc.) usando el módulo nativo `unicodedata`.

Luego de normalizar, se calcula la distancia de edición y se obtiene una métrica de **similitud porcentual**:

$$\text{Similitud (\%)} = \left(1 - \frac{\text{Distancia}}{\max(\text{longitud}(c_1), \text{longitud}(c_2))}\right) \times 100$$

Esto produce un valor intuitivo entre `0%` (sin coincidencia) y `100%` (cadenas equivalentes tras la normalización).

---

## 🧪 Pruebas y Resultados

El archivo `ejercicio6.py` incluye casos de prueba que cubren los distintos incisos del práctico:

| Caso analizado | Objetivo de la prueba |
| :--- | :--- |
| `"Juan Perez"` vs `"Jaun Perez"` | Demostrar la rigidez de Hamming ante transposición de caracteres. |
| `"Juan Perez"` vs `"Juan"` | Validar el fallo esperado en Hamming por diferencia de longitud. |
| `"Horacio López"` vs `"Oracio López"` | Probar la detección de omisión/inserción de caracteres con Levenshtein. |
| `"María Sol"` vs `"Maria Sol"` | Demostrar cómo la normalización de tildes logra un 100% de similitud. |
| `"Alejandro"` vs `"Alexander"` | Evaluar la similitud entre variantes de un mismo nombre. |

---

## 🚀 Cómo ejecutar el código

### Requisitos previos
* Tener instalado **Python 3.8** o superior.
* **No requiere instalar dependencias adicionales** (solo utiliza la biblioteca estándar de Python).

### Ejecución
1. Cloná este repositorio o descargá el archivo `ejercicio6.py`.
2. Abrí una terminal o consola de comandos en la carpeta del proyecto.
3. Ejecutá:
   ```bash
   python ejercicio6.py
   ```
   *(Si estás en Windows y `python` no está en tu PATH, podés usar `py ejercicio6.py`)*

---

## 📁 Estructura del Proyecto

```text
.
├── ejercicio6.py   # Implementación de Hamming, Levenshtein y heurística con casos de prueba
└── README.md        # Documentación general del ejercicio
```

---

