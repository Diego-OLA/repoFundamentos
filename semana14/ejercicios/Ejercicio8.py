productos = []
def agregar_producto(producto):
    if producto != None and producto != "":
        productos.append(producto)
    else:
        print("El producto no puede ser vacío.")

def buscar_producto(producto):
    for prod in productos:
        if prod == producto:
            return prod
    return False

op = 0
while op < 5:
    prod = input("Ingrese el nombre del producto a agregar: ")
    agregar_producto(prod)
    op += 1

   


prodBuscar = input("Ingrese el nombre del producto a buscar: ")
resultado = buscar_producto(prodBuscar)  
if resultado:
     print(f"Producto '{resultado}', en la lista")
else:        print(f"Producto '{prodBuscar}', no encontrado en la lista")
