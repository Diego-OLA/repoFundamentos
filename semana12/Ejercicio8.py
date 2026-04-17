lado1 = int(input("Ingresa el primer lado del triángulo: "))
lado2 = int(input("Ingresa el segundo lado del triángulo: "))
lado3 = int(input("Ingresa el tercer lado del triángulo: "))

if lado1 == lado2 == lado3:
    print("El triángulo es equilátero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("El triángulo es isósceles")
else:
    print("El triángulo es escaleno")