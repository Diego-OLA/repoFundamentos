suma = 0
numeros_validos = []

while suma <= 100:
    numero = int(input("Ingrese un número: "))

    if numero < 0:
        print("Número negativo ignorado")
        continue

    suma += numero
    numeros_validos.append(numero)

print("\nLa suma superó 100")
print("Números válidos ingresados:")

for num in numeros_validos:
    print(num)