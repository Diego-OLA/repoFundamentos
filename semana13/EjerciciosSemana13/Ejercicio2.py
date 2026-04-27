positivos = 0
negativos = 0
numero = None

while numero != 0:
    numero = int(input("Ingrese un número (0 para terminar): "))

    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

print("\nResumen:")

datos = [("Positivos", positivos), ("Negativos", negativos)]

for tipo, cantidad in datos:
    print(f"{tipo}: {cantidad}")