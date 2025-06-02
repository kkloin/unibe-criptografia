# Aplicativo de Cifrado César

Este es un aplicativo en Python que implementa el clásico **cifrado César**, una técnica de criptografía simétrica. Permite cifrar y descifrar mensajes en **español** o **inglés**, con desplazamientos definidos por el usuario.

## Características

* Cifrado y descifrado de mensajes.
* Soporte para idiomas: **Español** e **Inglés**.
* Permite elegir el desplazamiento (por ejemplo, +3 o +7).
* Mantiene las mayúsculas y caracteres especiales.
* Permite mostrar el mensaje cifrado en pantalla o guardarlo en un archivo `.txt`.

## Requisitos

* Python 3.6 o superior

## Instrucciones de uso

1. Clona el repositorio o descarga el archivo `caesar_cipher_app.py`.
2. Ejecuta el script desde la terminal:

   ```bash
   python cesar_cipher.py
   ```
3. Sigue las instrucciones que aparecen en pantalla:

   * Ingresa un mensaje de al menos 2 líneas.
   * Elige entre cifrar o descifrar.
   * Introduce el desplazamiento.
   * Selecciona el idioma.
   * Decide si quieres guardar el resultado o verlo en pantalla.

## Ejemplo de uso

```
Mensaje:
Hola mundo
Esta es la segunda línea

Operación: Cifrar
Desplazamiento: 3
Idioma: Español
```

**Resultado (ejemplo)**:

```
Krñd pxqgr
Hvwd hv od vhjxqgd ññhd
```

## Estructura del proyecto

```
|-- caesar_cipher.py           # Archivo principal del aplicativo
|-- caesar_cipher_app.py       # 2da versión del aplicativo
|-- README.md                  # Documentación del proyecto
```

## Licencia

Este proyecto se entrega bajo la licencia MIT. Puedes usarlo, modificarlo y distribuirlo libremente.

## Autor

Desarrollado por el Grupo #4 de la asignatura Criptografía como parte de una demostración de criptografía clásica.

