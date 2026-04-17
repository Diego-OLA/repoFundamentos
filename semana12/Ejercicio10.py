usuario = "user_admin"
password = "admin123"

usuarioIngresado = input("Ingrese su usuario: ")
passwordIngresada = input("Ingrese su contraseña: ")

if usuarioIngresado == usuario and passwordIngresada == password:
    print("Acesso permitido")
else:
    print("Acceso denegado")