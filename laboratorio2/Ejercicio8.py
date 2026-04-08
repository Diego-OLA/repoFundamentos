#Crear un programa con menú que permita al usuario ingresar un 
# texto y elegir una opción (1, 2 o 3). El programa debe usar 
# una función para aplicar la transformación seleccionada.
texto = input("Ingrese un texto: ")
opcion= int(input("Elige la opción 1, 2 o 3: ")) #Ing la verdad me perdi, pense que en alguno de los ejercicios
#anteriores tambien habia que pedirle la opcion al usuario, pero veo que solo en este esta especificando eso  :/
def convertir(txt,opc):
    match opc:
        case 1:
            print("Texto convertido a mayuscula: ", txt.upper())
           
        case 2:
            print("Texto convertido a minuscula: ",txt.lower())
        case 3:
            print("Texto convertido a primera mayuscula: ",txt.capitalize())


convertir(texto,opcion)
