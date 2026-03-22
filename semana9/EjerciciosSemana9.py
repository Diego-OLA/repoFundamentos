#Ejercicio 1
print("///////////////EJERCICIO 1//////////////////////")
nombre = input("Ingrese su nombre completo: ")

print("Mayúsculas:", nombre.upper())
print("Minúsculas:", nombre.lower())
print("Cantidad de caracteres:", len(nombre))


print(" ")
print("///////////////EJERCICIO 2//////////////////////")

#Ejercicio 2 

frase = input("Ingrese una frase: ")

print("Frase original:", frase)
print("Mayúsculas:", frase.upper())
print("Minúsculas:", frase.lower())

print(" ")
print("///////////////EJERCICIO 3//////////////////////")

#Ejercicio 3 

frase = input("Ingrese una frase: ")

sin_espacios = frase.replace(" ", "")
print("Cantidad de letras (sin espacios):", len(sin_espacios))


print(" ")
print("///////////////EJERCICIO 4//////////////////////")

#Ejercicio 4

correo = input("Ingrese un correo electrónico: ")

if "@" in correo:
    print("El correo parece válido")
else:
    print("El correo no es válido")

print(" ")
print("///////////////EJERCICIO 5//////////////////////")

#Ejercicio 5

frase = input("Ingrese una frase: ")

if len(frase) > 0:
    print("Primera letra:", frase[0])
    print("Última letra:", frase[-1])
else:
    print("La frase está vacía")


print("///////////////EJERCICIO 6//////////////////////")
nombre = input("Ingrese su nombre completo: ")

palabras = nombre.split()

for palabra in palabras:
    print(palabra)


print(" ")
print("///////////////EJERCICIO 7//////////////////////")

frase = input("Ingrese una frase: ")

nueva_frase = frase.replace("Python", "Programación")
print("Resultado:", nueva_frase)

print(" ")
print("///////////////EJERCICIO 8//////////////////////")

frase = input("Ingrese una frase: ")

cantidad = frase.count("a")
print("Cantidad de letras 'a':", cantidad)

print(" ")
print("///////////////EJERCICIO 9//////////////////////")

frase = input("Ingrese una frase: ")

if frase.startswith("Hola"):
    print("La frase empieza con 'Hola'")
else:
    print("La frase no empieza con 'Hola'")

print(" ")
print("///////////////EJERCICIO 10//////////////////////")

frase = input("Ingrese una frase: ")

if frase.endswith("."):
    print("La frase termina con un punto")
else:
    print("La frase no termina con un punto")
