cadena = "Python2026"

if cadena.isalnum():
    
    cadenaMinuscula = cadena.lower()
    resultado = cadenaMinuscula.replace("2026", "")
    
    print("Texto final:", resultado)
else:
    print("El texto no es alfanumérico")