Algoritmo laboratirio1
	// Este algoritmo realiza restas sucesivas
	// hasta que el resultado sea menor que 10.
	// Se utiliza la estructura Hacer-Mientras.
	Definir numeroIngresado Como Entero
	Escribir "Coloque un numero que sea mayor a 10 para restarlo hasta que el resultado sea menor a 10"
	Leer numeroIngresado
	
	//condicion que evalua que el valor que se ingreso sea mayor o igual a 10 
	si numeroIngresado >= 10 Entonces
		Mientras  numeroIngresado >= 10  Hacer  ///En el ciclo se va restando el numero ingresado por cada iteracion - 1 hasta que llega a ser 9
			
			numeroIngresado = numeroIngresado - 1
			Escribir numeroIngresado
			
			
		FinMientras
		
	SiNo
		Escribir "El valor ingresado debe ser igual o mayor a 10"
	
	
	FinSi
		
		
	
	

	
	
	
	
FinAlgoritmo
