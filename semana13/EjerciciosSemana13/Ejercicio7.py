notas = []
nota = 0

while nota != -1:
    nota = float(input("Ingrese una nota (-1 para terminar): "))

    if nota == -1:
        break

    if 0 <= nota <= 10:
        notas.append(nota)
    else:
        print("Nota inválida. Debe estar entre 0 y 10.")

suma = 0

for n in notas:
    suma += n

if len(notas) > 0:
    promedio = suma / len(notas)
    print(f"Promedio: {promedio}")
else:
    print("No se ingresaron notas válidas.")