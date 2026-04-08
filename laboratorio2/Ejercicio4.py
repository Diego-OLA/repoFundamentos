palabras = ["Mundial", "Resident Evil","hola Mundo"]
opcion = int(input("Seleccione una opcion 1,2 o 3: "))

def convertir(palabras,opc):
    resultado = [] 
    for palabra in palabras:
    
        if opc == 1:
        
            resultado.append(palabra.upper())  
        elif opc == 2:
                resultado.append(palabra.lower())  
        elif opc == 3:
                resultado.append(palabra.capitalize())  

    return resultado



conversion = convertir(palabras,opcion)
print(conversion)
