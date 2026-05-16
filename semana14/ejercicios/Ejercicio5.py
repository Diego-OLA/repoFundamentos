def obtener_positivos(numeros):
    positivos = []

    for numero in numeros:
        if numero > 0:
            positivos.append(numero)

    return positivos


numeros = [-5, 3, -2, 8, 0, 7, -1]
print("Números positivos:", obtener_positivos(numeros))