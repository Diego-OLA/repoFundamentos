#función que reciba un texto y una lista de números
#  (entre 1 y 3). La función debe aplicar cada transformación en orden y 
# devolver el resultado final.
lista = [3,1,2]  #al modificar la lista, modifica el orden en el que se aplican las corversiones
texto = "MunDIal 2026"  
def convertirSegunLista(txt,numerosLista):
    for numlista in numerosLista:
        match numlista:
            case 1:
                print("Texto MAYUSCULAS: ",txt.upper())
            case 2: 
                print("Texto minusculas: ",txt.lower())
            case 3: 
                print("Texto Capitalize: ",txt.capitalize())

convertirSegunLista(texto,lista)        