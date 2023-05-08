def cambioDePalabras(cadena,palabraVieja,palabraNueva):
    
    num_reemplazos = 0
    
    cantidad = cadena.count(palabraVieja)
    
    cadenaSpilt = cadena.split()
    
    for i in range(cantidad):
        localizar = cadenaSpilt.index(palabraVieja)
        cadenaSpilt.remove(palabraVieja)
        cadenaSpilt.insert(localizar,palabraNueva)
        num_reemplazos += 1
    
    
    return " ".join(cadenaSpilt) , num_reemplazos

cadena = "Hola como andas pinche Hola  Hola pendejo perro asquereso puto Hola Hola"
palabraBorrar = "Hola"
palabraNueva = "Puto"
cadenaNueva , cantidadBorradas = cambioDePalabras(cadena,palabraBorrar,palabraNueva)
print("Esta en la nueva cadena con la palabra borrada: ", cadenaNueva ,  " y la cantidad de veces que fue reemplazada fue de: ",cantidadBorradas, " veces!!")