Algoritmo AlgoritmoNumeroPositivoParcial
	Definir numeroIngresado, suma  Como Entero
	suma = 0
	numeroIngresado = 0
	
	Escribir "Al ingresar un numero negativo se detendrá la secuencia :)"
	Mientras numeroIngresado >= 0 Hacer
		Escribir "Introduzca un numero: "
		leer numeroIngresado
		si numeroIngresado >0 Entonces
			suma = numeroIngresado + suma
		SiNo
			Escribir "Fuera de la secuencia"
		FinSi
	FinMientras
	Escribir "La suma de la secuencia de numeros es: ",suma
	
FinAlgoritmo
