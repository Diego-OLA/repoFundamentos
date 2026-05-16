def ordenar_menor_mayor(numeros):
    n = len(numeros)

    for i in range(n):
        for j in range(n - 1):
            if numeros[j] > numeros[j + 1]:
                # Intercambiar valores
                aux = numeros[j]
                numeros[j] = numeros[j + 1]
                numeros[j + 1] = aux

    return numeros


numeros = []

for i in range(6):
    numero = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(numero)

print("Lista ordenada:", ordenar_menor_mayor(numeros))