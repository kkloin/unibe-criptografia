import math

def clean_text(text):
    """
    Limpia el texto eliminando espacios y convirtiendo a mayúsculas.
    Esto asegura uniformidad en el cifrado.
    """
    return ''.join(text.upper().split())

def create_transposition_matrix(text, key, fill_char='X'):
    """
    Crea una matriz para la transposición en columnas según la longitud de la clave.
    El texto se rellena con un carácter (por defecto 'X') si no llena completamente la matriz.
    """
    columns = len(key)
    rows = math.ceil(len(text) / columns)
    padded_text = text.ljust(rows * columns, fill_char)  # Rellenar con 'X' si es necesario

    # Crear la matriz dividiendo el texto en filas
    matrix = [list(padded_text[i:i + columns]) for i in range(0, len(padded_text), columns)]
    return matrix

def encrypt(text, key):
    """
    Cifra el texto usando transposición por columna simple.
    Se ordenan las columnas según el orden alfabético de la clave.
    """
    text = clean_text(text)
    matrix = create_transposition_matrix(text, key)

    # Obtener el orden de las columnas basado en la clave
    key_order = sorted(list(enumerate(key)), key=lambda x: x[1])

    cipher = ''
    # Leer las columnas en orden de la clave ordenada alfabéticamente
    for index, _ in key_order:
        for row in matrix:
            cipher += row[index]
    return cipher

def decrypt(ciphertext, key):
    """
    Descifra el texto cifrado utilizando la clave.
    Se reconstruye la matriz original y se lee fila por fila.
    """
    key_len = len(key)
    rows = math.ceil(len(ciphertext) / key_len)
    total_cells = rows * key_len

    # Inicializar columnas vacías
    cols = [''] * key_len

    # Orden alfabético de la clave
    sorted_key = sorted(list(enumerate(key)), key=lambda x: x[1])

    # Determinar cuántos caracteres va en cada columna
    col_lengths = [rows] * key_len
    extra_chars = total_cells - len(ciphertext)

    # Ajustar columnas que deben tener un carácter menos
    for i in range(extra_chars):
        col_lengths[sorted_key[-(i+1)][0]] -= 1

    # Llenar las columnas según el texto cifrado
    pos = 0
    for index, _ in sorted_key:
        length = col_lengths[index]
        cols[index] = list(ciphertext[pos:pos + length])
        pos += length

    # Leer la matriz fila por fila para reconstruir el mensaje original
    plaintext = ''
    for i in range(rows):
        for j in range(key_len):
            if i < len(cols[j]):
                plaintext += cols[j][i]
    return plaintext

def save_to_file(text, filename='output.txt'):
    """
    Guarda el resultado del cifrado o descifrado en un archivo .txt
    """
    with open(filename, 'w') as f:
        f.write(text)
    print(f"[✓] Mensaje guardado en {filename}")

def main():
    """
    Función principal del programa. Permite seleccionar entre cifrar o descifrar,
    ingresar texto, clave, y decidir si guardar el resultado en un archivo o mostrarlo.
    """
    print("🔐 Cifrado por Transposición de Columna Simple")
    option = input("¿Qué deseas hacer? (cifrar/descifrar): ").strip().lower()
    text = input("Introduce el mensaje: ")
    key = input("Introduce la clave (sin espacios): ").strip().upper()

    if option == 'cifrar':
        result = encrypt(text, key)
    elif option == 'descifrar':
        result = decrypt(text, key)
    else:
        print("❌ Opción no válida.")
        return

    output_option = input("¿Deseas guardar el resultado en un archivo? (sí/no): ").strip().lower()
    if output_option in ['sí', 'si', 's']:
        save_to_file(result)
    else:
        print(f"\n🔎 Resultado:\n{result}")

# Punto de entrada del programa
if __name__ == "__main__":
    main()
