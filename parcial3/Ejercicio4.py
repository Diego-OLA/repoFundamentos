for registro in range(1, 51):
    

    if registro == 42:
        print("Amenaza de seguridad detectada. Deteniendo auditoría.")
        break

    if registro % 3 == 0:
        continue
 #Evaluo primero registro == 42 porque 42 es multiplo de 3, entonces si pongo primero el 
 # if registro % 3 == 0, 
 # el programa se va a saltar el registro 42 y no va a detectar la amenaza de seguridad.
    

    # Procesar registros válidos
    print(f"Procesando registro ID: {registro}")