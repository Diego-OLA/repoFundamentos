def calcular_promedio(notas):
    suma = 0

    for nota in notas:
        suma += nota

    return suma / len(notas)


notas = [8, 7, 9, 6, 8]
promedio = calcular_promedio(notas)

print("Promedio:", promedio)

if promedio >= 6:
    print("El grupo aprueba.")
else:
    print("El grupo reprueba.")