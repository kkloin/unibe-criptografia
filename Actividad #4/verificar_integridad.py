mensaje_recibido = texto_cifrado
hash_recibido = hash_integridad

if hash_sha256(mensaje_recibido) == hash_recibido:
    print("Integridad verificada ✅")
else:
    print("⚠️ El mensaje ha sido alterado")
