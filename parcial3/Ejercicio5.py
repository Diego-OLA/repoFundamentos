nombre_completo = input("Ingrese su nombre completo (Nombre y Apellido): ")

# Convertir en lista y luego invertir el orden
partes = nombre_completo.split()
partes_invertidas = partes[::-1]

# Recorrer cada palabra (apellido y luego nombre)
for palabra in partes_invertidas:
    # Recorrer cada letra de la palabra
    for letra in palabra:
        print(letra, end=".")
    
    print()