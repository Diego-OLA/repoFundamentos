i= 0
while i < 27:
    print(f"Mes abril fecha{i}")
    i+= 1


#Hacer un juego de adivinar un numero
#el bucle tendra una variable en true
#El numero de intentos debe ser 10
#y  cuando tiene el numero que imprima lo lograste


condicion = False
intentos = 0

while condicion == False:
    if intentos == 10:
        print("Perdiste")
        break
    numero = int(input("Adivina el numero del 1 al 20: ") )
    if numero == 5:
        print("lo lograste")
        condicion = True

    elif numero < 0 or numero >20:
        print("No es valido el numero")
        intentos += 1
    else:
        print("Intentalo de nuevo")
        intentos += 1