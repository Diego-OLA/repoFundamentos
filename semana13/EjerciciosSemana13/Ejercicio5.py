contrasena_correcta = "12345678"
intentos_fallidos = 0
contrasena = ""

while contrasena != contrasena_correcta:
    contrasena = input("Ingrese la contraseña: ")

    if contrasena != contrasena_correcta:
        print("Contraseña incorrecta")
        intentos_fallidos += 1

print("\nAcceso concedido")
print("Intentos fallidos:")

for i in range(intentos_fallidos):
    print(f"Fallo #{i + 1}")