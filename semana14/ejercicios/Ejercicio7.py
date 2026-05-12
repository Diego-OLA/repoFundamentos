def contar_mayores_edad(edades):
    contador = 0

    for edad in edades:
        if edad >= 18:
            contador += 1

    return contador


edades = [15, 20, 17, 30, 18, 12, 25]
print("Mayores de edad:", contar_mayores_edad(edades))