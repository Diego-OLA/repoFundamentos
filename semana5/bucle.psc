	Algoritmo bucle
	//bucle es algo que se repite hasta que 
	//una condicion logica la rompe
	
	Definir contador Como Entero
	Escribir " numero del 0 al 100"
	Leer numeroEntrada
	contador = 0
	resultado = 0
	anterior = 0
	
	Mientras contador < numeroEntrada    //falso //null //unfined /7none
		anterior = resultado
		contador = contador + 1
		resultado = contador + anterior
		
		//0 ,1,2,...9,
		
		Escribir  "resultado es ", contador , " + ", anterior, "= ", resultado
	FinMientras
	
	Escribir "password "
	Leer pass
	
	Mientras pass <> "nombre de ella + fecha epecial"
		Escribir "romper bucle infinito 1 si 2 no "
		Leer respuesta
		si respuesta == "si"
			pass = "nombre de ella + fecha epecial"
		FinSi
	FinMientras
	
	Escribir "final "
	//exponentes
	//radicales
	//parentesis
	// di y mul
	//suma y resta
	//contador i i++ i--  contador =+ contador = contador + contador
	
FinAlgoritmo