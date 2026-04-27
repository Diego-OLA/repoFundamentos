Serie = "fullmetal alchemits"

### cada variable tiene un espacio de memoria asignado

## cuando una vable cambia => se pierde la inmutabilidad
## POO 
## polimorfismo -> es el cambio de acciones sin que se rompa el codigo 
## abstracciones -> 
##      Tasa de cafe   
#       cafe coscafe 
##       azucar 
##      agua 
##      otros ingredientes
##  un objeto es el que toma un modelo y este modelo le da funciones y utiliza sus propiedades

## Leon -> 
## tiene ojos  (propiedades)
## tiene boca 
## Esta guapo 
#############
#  corre        ( Funciones )
# salta 

## Clases
## Estructura de datos.


## es arreglo es una variable que tiene adentro otra variable
## Listas.
## Arrays.-> se inia a contar desde el 0
## tuplas.
## indices.


# -------------------------------------------------------
def saludo(nombres):
    print(nombres)


# saludo(Serie) las funciones simpre van  a tener ()
# -------------------------------------------------------
## las funciones tienen un espacio
## Scope es dond reciden las variables

## Colocar el nombre de la serie como titulo
fmaTemu = Serie.title()
saludo(Serie)
#saludo(fmaTemu)
fmaMayusculas = Serie.upper()
saludo(fmaMayusculas)


FullMetalCapitalizer = fmaMayusculas.swapcase().title()
saludo(FullMetalCapitalizer)

## deprogracion Lineal


##Comparar cadenas de texto

nombre = "Diego Omar Landaverde Ayala"
password = "123456"

if nombre == "Diego Omar Landaverde Ayala" :
    print("Ingrese su password")
    contra = str(input("ingrese su pass: "))
    if password == contra:
        print("Welcome to the Jungle")



comparar1 = "Diego"
comparar2 = "Diego"
# Usaremos para comparar y pasar a minusculas
variableTemporal  = comparar1.casefold()
print(variableTemporal)

#comparar = comparar1.casefold() == comparar2.casefold()
#print(comparar)

##casefold nos dara true unicamente si los elementos son identicos 

##isalfa() parar comparar numeros o signos especiales

clasicas2005 = "Gasolina 2025"

compararIsAlpha = clasicas2005.isalpha()
#print(compararIsAlpha) #da true cuando solo sean letras 

#Solo numero   isAlnum()
letraCancion = "Lo que paso paso entre tu y yo"
decada = "10"

ejemplo  = letraCancion.isalnum()
#print(ejemplo)
ejemplo = decada.isalnum() #da true cuando solo haya numero en el string de la variable
#print(ejemplo)



comprobarDecadas = decada.isdigit()

#isnumeric() sirve para evaluar cadenas de texto, muestra true si en una cadena solo hay numeros


jugadores = "Cristiano Leo song"
mayus = jugadores.isupper();
print(mayus)


controlEspacio = Serie.isspace()
print(controlEspacio)


#metodos de busqueda
tema = "En el bosque de china, la chinita se perdio "
temaf = tema.find("bosque")
print(temaf)

#rfind() permite hacer busqueda en caracteres empezando de derecha
temaf = tema.upper().rfind("BOSQUE");

print(temaf)

contador = tema.count("se")
contador = tema.startswith("En")
contador = tema.endswith("dio ")
temaModificado = tema.replace(" ","-")
print(temaModificado)