opcion= 3
def convertir(opc):
    texto = "mundial 2026"
    match opc:
        case 1:
            print( texto.upper())
           
        case 2:
            print(texto.lower())
        case 3:
            print(texto.capitalize())


convertir(opcion)
    