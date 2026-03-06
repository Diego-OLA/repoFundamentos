Algoritmo AlgoritmoNotas
	Definir nota Como Entero 
	
	Escribir "Ingresa la nota:"
	leer nota
	
	Si nota >= 6 Y nota <=10 Entonces
		Escribir 	"Aprobaste :)"
		
	FinSi
	si nota == 5 Entonces
		
		Escribir "Recuperación :("
	FinSi
	si nota <5 Y nota >= 0 Entonces
		Escribir "Reprobado :("
	SiNo
		Escribir "Solo se permiten notas del 0 al 10"
	FinSi
	
	
	
	
	
FinAlgoritmo
