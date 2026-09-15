# Ejercicio 4: Cálculo del Índice de Coincidencia (IC)

## ¿De qué trata?
Calcula el **Índice de Coincidencia (Index of Coincidence - IC)** de un texto dado. 

El IC es una medida estadística propuesta por William F. Friedman en criptoanálisis que representa la probabilidad de que **dos letras elegidas al azar de un texto sean idénticas**.

### Fundamento Teórico:
La fórmula aplicada es:
$$IC = \frac{\sum_{i=1}^{c} n_i (n_i - 1)}{N (N - 1)}$$

Donde:
- $n_i$: Frecuencia (apariciones) de cada carácter distinto en el texto.
- $N$: Longitud total del texto.

### Aplicación en Teoría de la Información y Criptografía:
- **Lenguaje Natural:** Debido a la redundancia del idioma, el texto plano en español o inglés tiene un IC característico alto ($\approx 0.065 - 0.075$).
- **Texto Aleatorio o Cifrado Polialfabético (ej. Vigenère):** Tiende a una distribución uniforme plana, bajando el IC hacia $1 / 26 \approx 0.0385$.

---

## Requisitos
- **Python 3.10 o superior**.
- **Dependencias:** Solo utiliza la biblioteca estándar (`pathlib`). No requiere instalar paquetes externos.

---

## Cómo ejecutarlo
Desde la terminal en la raíz del proyecto:
```powershell
python "Ejercicio 4/Ejercicio4.py"
```

El script solicitará la ruta del archivo de texto a analizar. Podés usar el archivo de prueba incluido:
- **Ruta:** `Ejercicio 4/EjemploEjercicio4.txt`
