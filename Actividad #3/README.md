# 🔐 Cifrado por transposición de columna simple

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
git clone https://github.com/kkloin/unibe-criptografia.git
cd transposicion_columna_simple
```

## ▶️ Ejecución
Desde la terminal, ejecuta:

```bash
python3 cifrado_transposicion.py
```

## 🧭 Instrucciones de uso
1. Al iniciar el programa:
Se te preguntará si deseas cifrar o descifrar un mensaje.

2. Luego:
Debes ingresar el texto a procesar (mensaje) y una clave (sin espacios, en mayúsculas o minúsculas).

3. Finalmente:
Puedes elegir si quieres mostrar el resultado por pantalla o guardarlo en un archivo _output.txt_.

## 🧪 Ejemplos de uso

**🔒 Cifrar un mensaje**
```bash
¿Qué deseas hacer? (cifrar/descifrar): cifrar
Introduce el mensaje: defensa en profundidad
Introduce la clave (sin espacios): CLAVE
¿Deseas guardar el resultado en un archivo? (sí/no): no

🔎 Resultado:
ENFDPRAODUENCESACIFX
```
**🔓 Descifrar un mensaje**
```bash
¿Qué deseas hacer? (cifrar/descifrar): descifrar
Introduce el mensaje: ENFDPRAODUENCESACIFX
Introduce la clave (sin espacios): CLAVE
¿Deseas guardar el resultado en un archivo? (sí/no): no

🔎 Resultado:
DEFENSAENPROFUNDIDAD
```
📌 Nota: Los espacios se eliminan al cifrar para simplificar el proceso. Puedes reinsertarlos manualmente si lo necesitas.

## 💾 Salida a archivo
Si eliges guardar el resultado, el programa lo escribirá automáticamente en _output.txt_ en el mismo directorio.
