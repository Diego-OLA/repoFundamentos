texto = input("Ingrese un texto: ")
opcion= int(input("Elige la opción 1, 2 o 3: "))
def convertir(txt,opc):
   
    match opc:
        case 1:
            print( txt.upper())
           
        case 2:
            print(txt.lower())
        case 3:
            print(txt.capitalize())


convertir(texto,opcion)