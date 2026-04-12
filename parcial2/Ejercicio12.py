archivo = "ING. Diego.txt"
sinExtension = archivo.removesuffix(".txt")
sinPrefijo = sinExtension.removeprefix("ING. ")

resultado = sinPrefijo.lower()

print("Texto final:", resultado)