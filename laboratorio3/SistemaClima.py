from datetime import datetime
#Campos del sistema de clima
#Dia, Maxima, Minima, temperaturaPromedio, Humedad, posiblidad lluvia.

op = -1
clima = {}
registros = []
def ingresar_datos():
    print("Ingrese los datos del clima: ")
   
    try:
        fecha = input("Ingrese la fecha (YYYY-MM-DD): ")
        maxima = float(input("Maxima: "))
        minima = float(input("Minima: ")) 
        temperatura_promedio = (maxima + minima) / 2
        humedad = float(input("Humedad: ")) 
        posiblidad_lluvia = float(input("Posibilidad de lluvia: "))
        datetime.strptime(fecha, "%Y-%m-%d") #valida si la fecha ingresada es valida, si no es valida se lanza una excepcion y se muestra un mensaje de error

    except ValueError:
        print("Fecha o demas datos no validos, por favor ingrese una fecha en el formato YYYY-MM-DD.")
        return #retorna para que no se agrgue el clima al registro si la fecha es ivalida
    
    if maxima > minima and 0 <= humedad <= 100 and 0 <= posiblidad_lluvia <= 100:
        clima= {

                    "fecha":fecha,
                    "maxima":maxima,
                    "minima":minima,
                    "temperatura_promedio":temperatura_promedio,
                    "humedad":humedad,
                    "posiblidad_lluvia":posiblidad_lluvia
            }
    else:
        print("Datos invalidos, por favor ingrese datos validos.")
        return #retorn para que no se agregue el clima al registro si los datos son invalidos
    #Agregamos el clima al registro
    registros.append(clima)
    ver_registro(clima["fecha"]) #retornamos clima y el arreglo con el registro de clima


def actualizar_registro(fecha):
    existRegistro = False
    for registro in registros:
        if registro["fecha"] == fecha.lower():
            print("Ingrese los nuevos datos del clima: ")
            try:
                maxima = float(input("Maxima: "))
                minima = float(input("Minima: ")) 
                temperatura_promedio = (maxima + minima) / 2
                humedad = float(input("Humedad: ")) 
                posiblidad_lluvia = float(input("Posibilidad de lluvia: "))
            except ValueError:
                print("Datos no validos, por favor ingrese datos validos.")
                return #retorna para que no se actualice el clima si los datos son invalidos
            
            if maxima > minima and 0 <= humedad <= 100 and 0 <= posiblidad_lluvia <= 100:
                registro["maxima"] = maxima
                registro["minima"] = minima
                registro["temperatura_promedio"] = temperatura_promedio
                registro["humedad"] = humedad
                registro["posiblidad_lluvia"] = posiblidad_lluvia
            else:
                print("Datos invalidos, por favor ingrese datos validos.")
                return #retorna para que no se actualice el clima si los datos son invalidos
            
            print("Registro actualizado: ", registro)
            existRegistro = True
            break
        
        else:
            existRegistro = False
    if  existRegistro == False:
        print("No se encontro un registro para el dia ingresado.")

def ver_registros():
    print("registros del clima: ")
    if len(registros) == 0:
            print("No hay registros de clima disponibles.")
    for registro in registros:
        print(registro)
       

def ver_registro(fecha):
    existRegistro = False
    for registro in registros:
        if registro["fecha"] == fecha.lower():
            print(registro)
            if registro["temperatura_promedio"] > 30:
                print("El clima es caluroso")
            elif registro["temperatura_promedio"] < 15:
                print("El clima es frio")
            else:
                print("El clima es templado")
            existRegistro = True
            break
        
        else:
            existRegistro = False
    if  existRegistro == False:
        print("No se encontro un registro para el dia ingresado.")
          
           

   

while op != 0:

    print("\n Bienvenido al sistema de clima ")
    print("Seleccione una opcion: ")
    print("1. Ingresar datos del clima")
    print("2. Ver datos del clima")
    print("3. Ver registro para un dia especifico")
    print("4. Actualizar registro existente")
    print("0. Salir")
    try:
        op = int(input("Opcion: "))
    except ValueError:
        print("Opcion no valida, por favor ingrese un numero.")
        continue


    match op:
        case 1:
            ingresar_datos()
        case 2:
            ver_registros()
        case 3:
            fecha = input("Ingrese la fecha (YYYY-MM-DD): ")
            ver_registro(fecha)
        case 4:
            fecha = input("Ingrese la fecha (YYYY-MM-DD): ")
            actualizar_registro(fecha)
        case 0:
            print("Saliendo del sistema de clima...")
        case _:
            print("Opcion no valida, por favor intente de nuevo.")


    

