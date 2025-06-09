# 🔐 Cifrado por Transposición de Columna Simple

Este proyecto es una aplicación en Python que implementa el algoritmo clásico de **cifrado por transposición de columna simple**.  
Permite cifrar y descifrar mensajes, con opción de guardar el resultado en un archivo de texto.

---

## 📘 Fundamento del método

La transposición por columna simple es un método criptográfico clásico que:
1. Escribe el mensaje en una matriz según la longitud de una clave.
2. Reordena las columnas siguiendo el orden alfabético de la clave.
3. El mensaje cifrado se genera leyendo columna por columna.

Para **descifrar**, se reconstruye la matriz usando la clave y se lee fila por fila.

---

## 🛠️ Requisitos

- Python 3.x
- Sistema compatible (Linux, macOS o Windows)

---

## 📥 Instalación

Clona este repositorio en tu máquina local:

```bash
git clone https://github.com/tu_usuario/transposicion_columna_simple.git
cd transposicion_columna_simple
