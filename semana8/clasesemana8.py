# las comillas triples son las que se encargan de hacer
# Cadenas de texto largas sin mdoficar el formato.
# texto corto
poema = (" Es porque un pajarito de la montaña ha hecho",)
"en el hueco de un árbol, su nido matinal"
"que el árbol amanece con música en el pecho",
"como que si tuviera corazón musical"


# textos largos ''' o """
poema = """Es porque un pajarito de la montaña ha hecho,
en el hueco de un árbol, su nido matinal,
que el árbol amanece con música en el pecho,
como que si tuviera corazón musical.

Si el dulce pajarito por entre el hueco asoma,
para beber rocío, para beber aroma,
el árbol de la sierra me da la sensación
de que se le ha salido, cantando, el corazón. """

#print(poema)

## computadora -> que variable queres imprimir
## print()

##MAYUSCULAS
##Mutabilidad -> siempre debemos evitar transformar objeto original
##clases -> estereotipo (como un molde)
##propiedades ->
##color 
##tipo de motor (Electrico o gas)

#ojos
#color de pelo

#funciones
#moverse
#frenar
#cargarse
#descargarse

poema_Mayusculas = poema.upper()
#print(poema_Mayusculas)
#convertir en minusculas
#string .lower
poema_minisculas = poema.lower()
#print(poema_minisculas)


mensaje  = "HolA que HaCE prOgramANDO O QUE hAcE"

mensaje_correcto = mensaje.capitalize()

print(mensaje_correcto)

#Las flipantes aventuras del gato con bolson magico y alfredo
titulo = "Las flipantes aventuras del gato con bolson magico y alfredo"
tituloCorrecto = titulo.title()


#swapCase permite cambiar entre mayusculas y minusculas

swapCaseTitulo = tituloCorrecto.swapcase()

print(swapCaseTitulo)

nombre = "Pepe"
nombre2 = "Juan"
comparar = nombre.casefold()==nombre2.casefold()

print(comparar)
