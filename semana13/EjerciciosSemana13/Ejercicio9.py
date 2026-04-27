import random

numero_secreto = random.randint(1, 20)
intentos = []
numero = None

while numero != numero_secreto:
    numero = int(input("Adivina el número (1-20): "))
    intentos.append(numero)

    if numero < numero_secreto:
        print("El número secreto es mayor")
    elif numero > numero_secreto:
        print("El número secreto es menor")

print("\n¡Correcto!")
print("Intentos realizados:")

for i, intento in enumerate(intentos, start=1):
    print(f"Intento {i}: {intento}")