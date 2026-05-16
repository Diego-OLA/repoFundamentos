#Codigos de rastro de envios
codigo = input("Ingrese el codigo de rastreo con el formato (AÑO-CATEGORIA-PAIS): ").upper()
if codigo == "" or codigo is None:
    print("Error: El código de rastreo no puede estar vacío.")

codigo_pais_split = codigo.split("-")

codigo_categoria = codigo_pais_split[1][0:]

#Para obtener el pais necesito partir de una manera que no sea estatica 
codigo_pais = codigo.split("-")[-1]

ruta = "Ruta local" if codigo_pais == "SV" else "Ruta internacional"

print(f"El código de rastreo es: {codigo}")
print(f"El código de categoría es: {codigo_categoria}")
print(f"El tipo de ruta es: {ruta}")