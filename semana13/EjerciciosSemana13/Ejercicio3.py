

num = 1

while num != -1:
    num = int(input("Ingrese un numero para generar la tabla(-1 para salir) "))
    

    for i in range(1,11):
        resultado =  num * i
        if resultado  > 20:
            print(f"{num} x {i} = {resultado} ")


