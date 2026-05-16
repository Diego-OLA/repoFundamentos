def encontrar_mayor(numeros):
    mayor = numeros[0]

    for numero in numeros:
        if numero > mayor:
            mayor = numero

    return mayor


numeros = []

for i in range(8):
    numero = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(numero)

print("El número mayor es:", encontrar_mayor(numeros))