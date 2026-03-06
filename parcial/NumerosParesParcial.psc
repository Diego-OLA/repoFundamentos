Algoritmo NumerosParesParcial
	//Crear un programa que reciba un número N y muestre los primeros N números pares usando un bucle para. ( modulo Para )
	Definir numeroIngresado, cantidadDePares, pares, contadorDePares Como Entero
	Escribir "Coloca un numero y obtendras la cantidad de numeros pares que tu pidas a continuación"
	
	Escribir "Escribe el numero a sacar numeros pares: "
	leer numeroIngresado
	Escribir "Elige la cantidad de pares (Si no hay esa cantidad de numeros pares te mostrará una validacion): "
	leer cantidadDePares
	contadorDePares = 0

	
	Definir i Como Entero
	Para i = 1 Hasta  numeroIngresado Con Paso 1 Hacer
		
		si numeroIngresado MOD 2 == 0 Y numeroIngresado > 0 Y contadorDePares < cantidadDePares
			pares = numeroIngresado
			Escribir pares
			contadorDePares = contadorDePares +1
		
	FinSi
	
		numeroIngresado = numeroIngresado -1
	FinPara
	
	Si contadorDePares < cantidadDePares 
		Escribir "No hay esa cantidad de pares, solo hay ", contadorDePares
		numeroIngresado = 3
	FinSi
	
	
	
	
	
FinAlgoritmo
