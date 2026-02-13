Algoritmo TotalPagar
	Definir  Precio Como Real
	Definir Cantidad Como Entero
	Definir Validacion Como Logico
	
	Escribir "Ingrese el precio del producto: " 
	leer Precio
	
	Escribir  "Cantidad de producto: "
	leer Cantidad
	
	Si Cantidad = 0  Entonces
		Escribir "la cantidad no puede ser 0"
		Validacion = Verdadero
		
		
	FinSi
	si Precio = 0
		Escribir "El precio no puede ser 0"
		Validacion = Verdadero
	FinSi
	
	Si Validacion = Falso 
		
		Escribir "El total es: ", Precio * Cantidad
	FinSi
	
	
	
FinAlgoritmo
