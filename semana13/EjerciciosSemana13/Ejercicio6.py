n = -1

while n != 0:
    n = int(input("Ingrese un número (0 para salir): "))

    if n == 0:
        break

    print("Números primos:")

    for num in range(1, n + 1):
        divisores = 0

        for i in range(1, num + 1):
            if num % i == 0:
                divisores += 1

        if divisores == 2:
            print(num)