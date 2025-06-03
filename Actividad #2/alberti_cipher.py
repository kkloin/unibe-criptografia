"""
Implementación del Cifrado de Alberti
=====================================

El cifrado de Alberti (1467) fue uno de los primeros sistemas de cifrado polialfabético.
Utiliza dos discos concéntricos: uno fijo (estacionario) y otro móvil.

Creado por: Leon Battista Alberti (1404-1472)
"""

class AlbertiCipher:
    def __init__(self):
        # Disco exterior (fijo) - Alfabeto del texto plano (mayúsculas)
        # Incluye números 1-4 como en el diseño original de Alberti
        self.outer_disk = "ABCDEFGHIKLMNOPQRSTVXZ1234"
        
        # Disco interior (móvil) - Alfabeto cifrado (minúsculas) 
        # Mezclado como en el diseño original, incluye "&" (et)
        self.inner_disk = "gklnprtuz&xysomqihfdbace"
        
        # Índice actual del disco móvil
        self.index_position = 0
    
    def set_index(self, key_letter):
        """
        Establece la posición del disco móvil alineando el índice con la letra clave.
        
        Args:
            key_letter (str): Letra del disco exterior para alinear con el índice
        """
        if key_letter.upper() not in self.outer_disk:
            raise ValueError(f"La letra clave '{key_letter}' no está en el disco exterior")
        
        # En el diseño original, 'g' es el índice del disco móvil
        index_char = 'g'
        index_pos_in_inner = self.inner_disk.index(index_char)
        key_pos_in_outer = self.outer_disk.index(key_letter.upper())
        
        # Calcular la nueva posición del disco móvil
        self.index_position = (key_pos_in_outer - index_pos_in_inner) % len(self.inner_disk)
    
    def get_rotated_inner_disk(self):
        """
        Retorna el disco interior en su posición actual.
        """
        return self.inner_disk[self.index_position:] + self.inner_disk[:self.index_position]
    
    def encrypt_char(self, char):
        """
        Cifra un solo carácter.
        
        Args:
            char (str): Carácter a cifrar
            
        Returns:
            str: Carácter cifrado
        """
        if char.upper() not in self.outer_disk:
            return char  # Retorna el carácter sin cambios si no está en el alfabeto
        
        outer_pos = self.outer_disk.index(char.upper())
        rotated_inner = self.get_rotated_inner_disk()
        
        return rotated_inner[outer_pos]
    
    def decrypt_char(self, char):
        """
        Descifra un solo carácter.
        
        Args:
            char (str): Carácter a descifrar
            
        Returns:
            str: Carácter descifrado
        """
        rotated_inner = self.get_rotated_inner_disk()
        
        if char not in rotated_inner:
            return char  # Retorna el carácter sin cambios si no está en el alfabeto
        
        inner_pos = rotated_inner.index(char)
        return self.outer_disk[inner_pos]
    
    def encrypt(self, plaintext, key_changes=None):
        """
        Cifra un mensaje completo.
        
        Args:
            plaintext (str): Texto a cifrar
            key_changes (dict): Diccionario {posición: nueva_letra_clave} para cambios de clave
                               Ejemplo: {5: 'R', 10: 'S'} cambia la clave en posición 5 y 10
        
        Returns:
            str: Texto cifrado
        """
        if key_changes is None:
            key_changes = {}
        
        ciphertext = []
        
        for i, char in enumerate(plaintext):
            # Verificar si hay un cambio de clave en esta posición
            if i in key_changes:
                self.set_index(key_changes[i])
                ciphertext.append(key_changes[i])  # Añadir la letra clave al texto cifrado
            
            # Cifrar el carácter actual
            encrypted_char = self.encrypt_char(char)
            ciphertext.append(encrypted_char)
        
        return ''.join(ciphertext)
    
    def decrypt(self, ciphertext, initial_key='A'):
        """
        Descifra un mensaje completo.
        
        Args:
            ciphertext (str): Texto cifrado
            initial_key (str): Letra clave inicial
        
        Returns:
            str: Texto descifrado
        """
        self.set_index(initial_key)
        plaintext = []
        i = 0
        
        while i < len(ciphertext):
            char = ciphertext[i]
            
            # Verificar si es una letra clave (mayúscula)
            if char.isupper() and char in self.outer_disk:
                # Cambiar la posición del disco
                self.set_index(char)
                i += 1
                continue
            
            # Descifrar el carácter
            decrypted_char = self.decrypt_char(char)
            plaintext.append(decrypted_char)
            i += 1
        
        return ''.join(plaintext)
    
    def display_disk_state(self):
        """
        Muestra el estado actual de los discos.
        """
        rotated_inner = self.get_rotated_inner_disk()
        
        print("Estado actual de los discos de Alberti:")
        print("=" * 50)
        print("Disco exterior (fijo):")
        print(' '.join(self.outer_disk))
        print("\nDisco interior (móvil - posición actual):")
        print(' '.join(rotated_inner))
        print(f"\nÍndice 'g' alineado con: {self.outer_disk[self.inner_disk.index('g') - self.index_position]}")
        print("=" * 50)


def demo_alberti():
    """
    Demostración del cifrado de Alberti.
    """
    print("DEMOSTRACIÓN DEL CIFRADO DE ALBERTI")
    print("=" * 50)
    
    cipher = AlbertiCipher()
    
    # Ejemplo 1: Cifrado básico
    print("\n1. CIFRADO BÁSICO")
    print("-" * 20)
    cipher.set_index('A')
    mensaje = "HOLA MUNDO"
    cifrado = cipher.encrypt(mensaje)
    print(f"Mensaje original: {mensaje}")
    print(f"Mensaje cifrado:  {cifrado}")
    
    # Descifrado
    descifrado = cipher.decrypt(cifrado, 'A')
    print(f"Mensaje descifrado: {descifrado}")
    
    # Ejemplo 2: Con cambios de clave (como en el método original de Alberti)
    print("\n2. CIFRADO CON CAMBIOS DE CLAVE")
    print("-" * 35)
    mensaje2 = "ESTE ES UN MENSAJE SECRETO"
    cambios_clave = {10: 'R', 20: 'S'}  # Cambiar clave en posición 10 y 20
    cipher.set_index('B')  # Clave inicial
    cifrado2 = cipher.encrypt(mensaje2, cambios_clave)
    print(f"Mensaje original: {mensaje2}")
    print(f"Mensaje cifrado:  {cifrado2}")
    
    # Descifrado
    descifrado2 = cipher.decrypt(cifrado2, 'B')
    print(f"Mensaje descifrado: {descifrado2}")
    
    # Mostrar estado de los discos
    print("\n3. ESTADO DE LOS DISCOS")
    print("-" * 25)
    cipher.set_index('A')
    cipher.display_disk_state()


if __name__ == "__main__":
    demo_alberti() 