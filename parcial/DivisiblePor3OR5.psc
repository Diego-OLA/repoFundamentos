Algoritmo DivisiblePor3OR5
	Definir numeroIngresado Como Entero
	Definir condicion Como Logico
	Escribir "Si ingresa un numero divisible por 3 o 5 obtendra verdadero"
	
	leer numeroIngresado
	condicion = Falso
	si  numeroIngresado <> 0  Y (numeroIngresado MOD 3 == 0 o numeroIngresado MOD 5 == 0)   Entonces
		
		condicion = Verdadero
		Escribir condicion
	SiNo
		Escribir condicion 
	FinSi
FinAlgoritmo
