import numpy as np
import hashlib

ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def cifrado_cesar(texto, desplazamiento):
    resultado = ""
    for c in texto.upper():
        if c in ABC:
            idx = (ABC.index(c) + desplazamiento) % 26
            resultado += ABC[idx]
        else:
            resultado += c
    return resultado

def descifrado_cesar(texto, desplazamiento):
    return cifrado_cesar(texto, -desplazamiento)

def texto_a_vectores(texto, n):
    while len(texto) % n != 0:
        texto += 'X'  # Relleno
    vectores = []
    for i in range(0, len(texto), n):
        vectores.append([ABC.index(c) for c in texto[i:i+n]])
    return vectores

def vectores_a_texto(vectores):
    return ''.join(ABC[num % 26] for vec in vectores for num in vec)

def cifrado_hill(texto, matriz_clave):
    n = matriz_clave.shape[0]
    vectores = texto_a_vectores(texto, n)
    resultado = []
    for vec in vectores:
        producto = np.dot(matriz_clave, vec) % 26
        resultado.append(producto.astype(int))
    return vectores_a_texto(resultado)

def inversa_modular_matriz(matriz, modulo):
    det = int(round(np.linalg.det(matriz))) % modulo
    inv_det = pow(det, -1, modulo)
    adjunta = np.round(det * np.linalg.inv(matriz)).astype(int) % modulo
    return (inv_det * adjunta) % modulo

def descifrado_hill(texto, matriz_clave):
    inv = inversa_modular_matriz(matriz_clave, 26)
    return cifrado_hill(texto, inv)

def hash_sha256(texto):
    return hashlib.sha256(texto.encode()).hexdigest()
