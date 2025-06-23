
# 🔐 Cifrado combinado por sustitución y matrices en Linux

## Descripción

Este proyecto implementa un sistema de cifrado y descifrado que combina dos técnicas clásicas de criptografía:

- **Cifrado por sustitución tipo César**: desplaza cada letra del mensaje un número fijo de posiciones en el alfabeto.
- **Cifrado por matrices tipo Hill**: aplica una transformación matricial invertible sobre bloques de texto para aumentar la difusión y complejidad.

El programa está desarrollado en Python y puede ejecutarse fácilmente en entornos Linux. Además, incluye una función opcional para validar la integridad del mensaje mediante un hash SHA-256.
---

## 🛠️ Requisitos

- Python 3.7 o superior.
- Librería `numpy` (para operaciones matriciales).

Para instalar numpy, ejecuta:
```bash
pip install numpy
```

## 🐍 Script en Python: cifrado_comb.py

# Funcionalidades:
```bash
- cifrar(mensaje, desplazamiento, matriz_clave)
- descifrar(mensaje_cifrado, desplazamiento, matriz_clave)
- verificar_integridad(mensaje_original, hash_original)
```

## 📋 Pruebas realizadas (ejemplo en consola)

1. Mensaje original:
```bash
ATAQUEALAMANANA
```

2. Parámetros:
```bash
desplazamiento = 3
matriz_clave = np.array([[3, 3], [2, 5]])
```

3. Ejecución:
```bash
texto_cesar = cifrado_cesar("ATAQUEALAMANANA", desplazamiento)
texto_cifrado = cifrado_hill(texto_cesar, matriz_clave)
hash_integridad = hash_sha256(texto_cifrado)
```

4. Verificación:
```bash
# Descifrado
desc_hill = descifrado_hill(texto_cifrado, matriz_clave)
desc_final = descifrado_cesar(desc_hill, desplazamiento)
```

## 🔐 Seguridad del contenido cifrado:
- Cifrado doble: se aplica una capa de sustitución (confusión) seguida de una transformación lineal (difusión).
- Matrices invertibles: aseguran que la operación sea reversible y no pierda información.
- Aritmética modular: evita desbordamientos y se adapta a la lógica de alfabetos finitos.
- Validación SHA-256: permite verificar que el mensaje no fue modificado en tránsito.

## ✅ Validación de integridad (opcional):
```bash
mensaje_recibido = texto_cifrado
hash_recibido = hash_integridad

if hash_sha256(mensaje_recibido) == hash_recibido:
    print("Integridad verificada ✅")
else:
    print("⚠️ El mensaje ha sido alterado")
```
