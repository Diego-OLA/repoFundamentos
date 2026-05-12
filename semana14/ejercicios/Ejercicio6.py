import random


def contar_mayores_50(numeros):
    contador = 0

    for numero in numeros:
        if numero > 50:
            contador += 1

    return contador


numeros = []

for i in range(10):
    numeros.append(random.randint(1, 100))

print("Números generados:", numeros)
print("Cantidad mayores a 50:", contar_mayores_50(numeros))