# Teoría de la Información - Practica 1
**Universidad Nacional de San Juan (UNSJ)**  
*Licenciatura en Ciencias de la Computación*
### Integrantes (Grupo 8):
- **Bravo**, Hernán
- **Cattaneo**, Jeremías
- **Nehin**, José
- **Quiroga**, Juan Marcos


---

##  Índice General de Ejercicios

| # | Ejercicio | Tema Principal | Comando de Ejecución |
|---|---|---|---|
| **01** | [Ejercicio 1](./Ejercicio%201/) | **Audio y Entropía:** Comparación de entropía y redundancia en archivos WAV (sin compresión) vs. MP3 (comprimido). | `python "Ejercicio 1/Ejercicio1.py"` |
| **02** | [Ejercicio 2](./Ejercicio%202/) | **Imágenes y Entropía:** Análisis de cabeceras y distribución de bytes en imágenes BMP vs. JPG con gráficos en Matplotlib. | `python "Ejercicio 2/Ejercicio2.py"` |
| **03** | [Ejercicio 3](./Ejercicio%203/) | **Texto y Redundancia:** Cálculo de entropía de Shannon y redundancia en archivos de texto plano (.txt) vs. comprimidos (.rar). | `python "Ejercicio 3/Ejercicio3.py"` |
| **04** | [Ejercicio 4](./Ejercicio%204/) | **Índice de Coincidencia (IC):** Medida estadística de Friedman para detección de redundancia lingüística y criptoanálisis. | `python "Ejercicio 4/Ejercicio4.py"` |
| **05** | [Ejercicio 5](./Ejercicio%205/) | **Bitmasking y Serialización:** Empaquetamiento de 8 booleanos en 1 byte y comparativa de almacenamiento JSON vs. binario (.bin). | `python "Ejercicio 5/main.py"` |
| **06** | [Ejercicio 6](./Ejercicio%206/) | **Distancias entre Cadenas:** Implementación de Distancia de Hamming (sustituciones) y Levenshtein (edición dinámica). | `python "Ejercicio 6/ejercicio6.py"` |
| **07** | [Ejercicio 7](./Ejercicio%207/) | **Detección de Errores (Módulo 11):** Validación y generación del dígito verificador para CUIT/CUIL. | `python "Ejercicio 7/Ejercicio7.py"` |
| **08** | [Ejercicio 8](./Ejercicio%208/) | **Capacidad de Canal (Optimización):** Búsqueda exhaustiva de la distribución de entrada óptima $P(X)$ que maximiza $I(X; Y)$. | `python "Ejercicio 8/ejercicio8.py"` |
| **09** | [Ejercicio 9](./Ejercicio%209/) | **Canal BSC con Sockets TCP:** Simulación cliente-servidor, estimación de BER empírico, matriz de canal, información mutua y capacidad. | *Server:* `python "Ejercicio 9/Servidor/main.py"`<br>*Client:* `python "Ejercicio 9/Cliente/main.py"` |

---

## ⚙️ Requisitos Globales
- **Python 3.10 o superior**
- **Librerías externas:**
  ```powershell
  pip install matplotlib
  ```
  *(Utilizada en los Ejercicios 1 y 2 para la graficación de distribuciones de frecuencia).*
