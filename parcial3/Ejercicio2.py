#Terminal de cobro 
import decimal


num = 1
total = decimal.Decimal(0)
while num == 1:
    monto = input("Ingrese el monto a cobrar (0 para salir del sistema): ")

    try:
        monto = decimal.Decimal(monto)
       
        if monto == 0:
            print("Saliendo del sistema de cobro. ¡Hasta luego!")
            num = 0
            break
        total =  total+ monto 
       

    except decimal.InvalidOperation:
        print("Error: El monto ingresado no es válido. Por favor, ingrese un número decimal.")
        continue


print(f"El monto total es: {total}")