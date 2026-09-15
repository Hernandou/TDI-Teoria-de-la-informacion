# Ejercicio 5: Empaquetamiento de Bits y Comparación de Formatos

## ¿De qué trata?
Demuestra la optimización de almacenamiento mediante **máscaras de bits (Bitmasking)**:
- Empaqueta **8 atributos booleanos** de una persona en **un único byte** (8 bits).
- Compara el costo de almacenamiento generando dos archivos en `Ejercicio 5/files/`:
  - `jsonyDataPersons.json`: Formato texto con nombres de claves repetidos (alta redundancia).
  - `binaryDataPersons.bin`: Formato binario compacto serializado con `pickle`.

## Requisitos
- Python 3.x (solo bibliotecas estándar: `json`, `pickle`). No requiere `pip install`.

## Cómo ejecutarlo
Desde la terminal en la raíz del proyecto:
```powershell
python "Ejercicio 5/main.py"
```

**Opciones:**
- **1:** Cargar personas (manualmente o desde `personas.json`).
- **2:** Generar archivos en la carpeta `files/`.
- **3:** Salir.
