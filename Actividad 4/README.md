
# Proyecto: Cifrado combinado por sustitución y matrices en Linux

## Descripción

Este proyecto implementa un sistema de cifrado y descifrado que combina dos técnicas clásicas de criptografía:

- **Cifrado por sustitución tipo César**: desplaza cada letra del mensaje un número fijo de posiciones en el alfabeto.
- **Cifrado por matrices tipo Hill**: aplica una transformación matricial invertible sobre bloques de texto para aumentar la difusión y complejidad.

El programa está desarrollado en Python y puede ejecutarse fácilmente en entornos Linux. Además, incluye una función opcional para validar la integridad del mensaje mediante un hash SHA-256.

---

## Requisitos

- Python 3.7 o superior
- Librería `numpy` (para operaciones matriciales)

Para instalar numpy, ejecuta:
```bash
pip install numpy
