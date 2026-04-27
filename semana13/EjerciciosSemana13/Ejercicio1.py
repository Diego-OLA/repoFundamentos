numero = -1

while numero != 0:
    numero = int(input("Ingrese un número (0 para salir): "))

    if numero == 0:
        break

    print("Números pares:")

    for i in range(1, numero + 1):
        if i % 2 == 0:
            print(i)