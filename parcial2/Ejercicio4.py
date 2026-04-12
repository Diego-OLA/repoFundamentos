palabra = "CANTANDO"
palabraMinus = palabra.lower()
palabraSinSufijo = palabraMinus.removesuffix("ando")
indice_t = palabraSinSufijo.find("t")

print(palabraSinSufijo)
print(indice_t)