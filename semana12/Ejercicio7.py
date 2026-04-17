compra = int(input("Ingresa el monto de tu compra: "))

if compra > 100:
    print("Tienes un descuento del 20%")
elif compra < 100 and compra >50:
    print("Tienes un descuento del 10%")
elif compra < 50:
    print("No hay descuento")
else:
    print("Monto no válido")