

num = -1
numeros= []
suma = 0
while num != 0:
    num = int(input("Ingrese un numero impar (0 para salir) "))
    if num%2 != 0:
        suma = suma +num
        numeros.append(num)
      
    



for i in numeros:
    print(f"numeros impares ingresados: {i}")

print(f"Valor de los numeros impares sumados: {suma}")  