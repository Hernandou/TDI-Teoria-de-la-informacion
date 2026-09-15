# Ejercicio 9: Canal Binario Simétrico (BSC) con Sockets TCP

## ¿De qué trata?
Simula un **Canal Binario Simétrico (BSC)** mediante una arquitectura Cliente-Servidor TCP:
1. **Descubrimiento de la probabilidad de error ($p$):** El servidor actúa como caja negra con $p$ oculta. El cliente envía tramas aleatorias (100, 10.000 y 1.000.000 de bits) y calcula el **BER empírico**, observando cómo converge a $p \approx 0.06$ por la Ley de los Grandes Números.
2. **Efecto visual del ruido:** Convierte una frase a binario (ASCII de 8 bits), la envía por el canal y muestra en pantalla cómo el texto recibido llega alterado.
3. **Modelado Teórico:**
   - Construye la **Matriz de Transición del Canal**.
   - Calcula la **Información Mutua** $I(A,B) = H(B) - H(B/A)$.
   - Calcula la **Capacidad del Canal** $C = 1 - H(p)$.
   - Demuestra que con tramas equiprobables ($P(0) \approx P(1) \approx 0.5$) se maximiza el canal: $I(A,B) \approx C$.

## Requisitos
- Python 3.x (solo bibliotecas estándar: `socket`, `struct`, `math`, `random`).

## Cómo ejecutarlo
Se necesitan **dos terminales abiertas en simultáneo**:

**1. Terminal 1 (Servidor):**
```powershell
python "Ejercicio 9/Servidor/main.py"
```

**2. Terminal 2 (Cliente):**
```powershell
python "Ejercicio 9/Cliente/main.py"
```

**Opciones del menú del cliente:**
- **1:** Enviar frase de texto (muestra el mensaje enviado y el recibido alterado).
- **2:** Enviar batería de bits aleatorios (100, 10.000 o 1.000.000 bits) para calcular BER, Matriz, $I(A,B)$ y Capacidad.
- **3:** Salir.
