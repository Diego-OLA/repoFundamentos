num = 1

while num != 0:
    num = int(input("Ingresa un número impar (0 para salir): "))

    if num == 0:
        break

    for i in range(1, num + 1, 2):
        print(("*" * i).center(num))