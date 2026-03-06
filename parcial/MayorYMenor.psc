Algoritmo MayorYMenor
	Definir numeroIngresado1, numeroIngresado2, numeroMayor, numeroMenor Como Entero
	
	Escribir "Ingrese dos cantidades y el algoritmo determinará cual es el mayor y menor"
	
	Escribir "Primera cantidad: "
	leer numeroIngresado1
	Escribir "Segunda cantidad: "
	leer numeroIngresado2
	
	si numeroIngresado1 > numeroIngresado2 Entonces
		numeroMayor = numeroIngresado1
		numeroMenor = numeroIngresado2
		
		Escribir "El numero mayor es :",numeroMayor
		Escribir "El numero menor es :",numeroMenor
	
	SiNo
		si numeroIngresado1 < numeroIngresado2
			numeroMayor = numeroIngresado2
			numeroMenor = numeroIngresado1
			Escribir "El numero mayor es :",numeroMayor
			Escribir "El numero menor es :",numeroMenor
		SiNo
			Escribir "Ambos numeros son iguales"
		FinSi
		
		
	FinSi
	
FinAlgoritmo

