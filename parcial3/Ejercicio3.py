#lecturas de temperatura
temperaturas = []
while len(temperaturas) < 5:
    try:
        temperatura = int(input("Ingrese la temperatura en grados Celsius: "))
        temperaturas.append(temperatura)
    except ValueError:
        print("Error: La temperatura ingresada no es un número entero válido.")



for temp in temperaturas:
    estado = "Estado estable" if temp >=10 and temp <= 30 else "Estado critico"
    match temp:
        case 0:
            print("Punto de congelación.")
        case 100:
            print("Punto de ebullición.")
        case _:
            print(estado)


