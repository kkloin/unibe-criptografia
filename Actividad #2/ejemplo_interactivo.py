"""
Ejemplo Interactivo del Cifrado de Alberti
==========================================

Este script permite al usuario experimentar con el cifrado de Alberti
de manera interactiva.
"""

from alberti_cipher import AlbertiCipher

def mostrar_menu():
    """Muestra el menú principal."""
    print("\n" + "="*60)
    print("         CIFRADO DE ALBERTI - MENÚ INTERACTIVO")
    print("="*60)
    print("1. Cifrar un mensaje")
    print("2. Descifrar un mensaje")
    print("3. Ver estado de los discos")
    print("4. Información sobre el cifrado de Alberti")
    print("5. Ejemplo rápido")
    print("6. Salir")
    print("="*60)

def cifrar_mensaje():
    """Función para cifrar un mensaje."""
    cipher = AlbertiCipher()
    
    print("\n--- CIFRAR MENSAJE ---")
    mensaje = input("Ingresa el mensaje a cifrar: ").upper()
    
    # Configurar clave inicial
    clave_inicial = input("Ingresa la letra clave inicial (A-Z, default=A): ").upper()
    if not clave_inicial:
        clave_inicial = 'A'
    
    # Preguntar si quiere cambios de clave
    usar_cambios = input("¿Quieres usar cambios de clave durante el cifrado? (s/n, default=n): ").lower()
    
    cambios_clave = {}
    if usar_cambios == 's':
        print("Formato: posición:letra (ej: 5:R, 10:S)")
        print("Deja vacío para terminar")
        while True:
            cambio = input("Cambio de clave (posición:letra): ")
            if not cambio:
                break
            try:
                pos, letra = cambio.split(':')
                cambios_clave[int(pos)] = letra.upper()
            except:
                print("Formato incorrecto. Usa: posición:letra")
    
    cipher.set_index(clave_inicial)
    cifrado = cipher.encrypt(mensaje, cambios_clave)
    
    print(f"\nMensaje original:  {mensaje}")
    print(f"Mensaje cifrado:   {cifrado}")
    print(f"Clave inicial:     {clave_inicial}")
    if cambios_clave:
        print(f"Cambios de clave:  {cambios_clave}")

def descifrar_mensaje():
    """Función para descifrar un mensaje."""
    cipher = AlbertiCipher()
    
    print("\n--- DESCIFRAR MENSAJE ---")
    mensaje_cifrado = input("Ingresa el mensaje cifrado: ")
    
    clave_inicial = input("Ingresa la letra clave inicial (A-Z, default=A): ").upper()
    if not clave_inicial:
        clave_inicial = 'A'
    
    descifrado = cipher.decrypt(mensaje_cifrado, clave_inicial)
    
    print(f"\nMensaje cifrado:    {mensaje_cifrado}")
    print(f"Mensaje descifrado: {descifrado}")
    print(f"Clave inicial:      {clave_inicial}")

def mostrar_estado_discos():
    """Muestra el estado actual de los discos."""
    cipher = AlbertiCipher()
    
    print("\n--- ESTADO DE LOS DISCOS ---")
    clave = input("Ingresa una letra para posicionar el disco (A-Z, default=A): ").upper()
    if not clave:
        clave = 'A'
    
    cipher.set_index(clave)
    cipher.display_disk_state()

def mostrar_informacion():
    """Muestra información sobre el cifrado de Alberti."""
    print("\n" + "="*60)
    print("         INFORMACIÓN DEL CIFRADO DE ALBERTI")
    print("="*60)
    print("""
El cifrado de Alberti fue inventado por Leon Battista Alberti en 1467
y es considerado el primer sistema de cifrado polialfabético de la historia.

CARACTERÍSTICAS PRINCIPALES:
• Utiliza dos discos concéntricos: uno fijo (exterior) y uno móvil (interior)
• El disco exterior contiene el alfabeto del texto plano (mayúsculas)
• El disco interior contiene un alfabeto mezclado para el cifrado (minúsculas)
• Se pueden cambiar las posiciones del disco durante el cifrado
• Esto hace que la misma letra pueda cifrarse de diferentes maneras

VENTAJAS:
• Más seguro que los cifrados monoalfabéticos
• Resiste al análisis de frecuencias básico
• Fue revolucionario para su época

ALFABETOS UTILIZADOS EN ESTA IMPLEMENTACIÓN:
• Disco exterior (fijo):     {outer_disk}
• Disco interior (móvil):    {inner_disk}

FUNCIONAMIENTO:
1. Se alinea el índice 'g' del disco móvil con una letra clave del disco fijo
2. Cada letra del mensaje se cifra usando la correspondencia actual de los discos
3. Se pueden cambiar las posiciones durante el cifrado para mayor seguridad
    """.format(
        outer_disk="ABCDEFGHIKLMNOPQRSTVXZ1234",
        inner_disk="gklnprtuz&xysomqihfdbace"
    ))

def ejemplo_rapido():
    """Ejecuta un ejemplo rápido del cifrado."""
    print("\n--- EJEMPLO RÁPIDO ---")
    
    cipher = AlbertiCipher()
    
    # Ejemplo 1: Cifrado simple
    print("1. CIFRADO SIMPLE:")
    mensaje1 = "HOLA"
    cipher.set_index('A')
    cifrado1 = cipher.encrypt(mensaje1)
    descifrado1 = cipher.decrypt(cifrado1, 'A')
    
    print(f"   Mensaje:    {mensaje1}")
    print(f"   Cifrado:    {cifrado1}")
    print(f"   Descifrado: {descifrado1}")
    
    # Ejemplo 2: Con cambios de clave
    print("\n2. CIFRADO CON CAMBIOS DE CLAVE:")
    mensaje2 = "SECRETO"
    cambios = {3: 'R'}  # Cambiar clave en posición 3
    cipher.set_index('B')
    cifrado2 = cipher.encrypt(mensaje2, cambios)
    descifrado2 = cipher.decrypt(cifrado2, 'B')
    
    print(f"   Mensaje:    {mensaje2}")
    print(f"   Cifrado:    {cifrado2}")
    print(f"   Descifrado: {descifrado2}")
    print(f"   Cambio:     Posición 3 -> clave 'R'")

def main():
    """Función principal del programa interactivo."""
    print("¡Bienvenido al Cifrado de Alberti!")
    print("Implementación del primer sistema polialfabético de la historia (1467)")
    
    while True:
        mostrar_menu()
        try:
            opcion = input("\nSelecciona una opción (1-6): ")
            
            if opcion == '1':
                cifrar_mensaje()
            elif opcion == '2':
                descifrar_mensaje()
            elif opcion == '3':
                mostrar_estado_discos()
            elif opcion == '4':
                mostrar_informacion()
            elif opcion == '5':
                ejemplo_rapido()
            elif opcion == '6':
                print("\n¡Gracias por usar el Cifrado de Alberti!")
                print("¡Que tengas un buen día!")
                break
            else:
                print("\nOpción no válida. Por favor selecciona 1-6.")
                
        except KeyboardInterrupt:
            print("\n\n¡Programa interrumpido por el usuario!")
            break
        except Exception as e:
            print(f"\nError: {e}")

if __name__ == "__main__":
    main() 