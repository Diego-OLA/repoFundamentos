#función que reciba un texto y un número, transforme el texto según 
# la opción y luego devuelva la cantidad de caracteres del resultado.
texto = input("Ingrese un texto: ")
opcion= int(input("Elige la opción 1, 2 o 3: "))
def convertir(txt,opc):
    print("Longitud del texto: ", len(txt))
    match opc:
        case 1:
            print("Texto convertido a mayuscula: ", txt.upper())
           
        case 2:
            print("Texto convertido a minuscula: ",txt.lower())
        case 3:
            print("Texto convertido a primera mayuscula: ",txt.capitalize())


convertir(texto,opcion)
