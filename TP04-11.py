"""TP04-11 | REEMPLAZO DE PALABRA
Desarrollar una función para reemplazar todas las apariciones de una palabra por otra en una cadena de caracteres
y devolver la cadena obtenida y un entero con la cantidad de reemplazos realizados.
Tener en cuenta que sólo deben reemplazarse palabras completas, y no fragmentos de palabras.
Escribir también un programa para verificar el comportamiento de la función."""

def cambioDePalabras(cadena,palabraVieja,palabraNueva):
    
    cadenaSpilt = cadena.split()
    
    num_reemplazos = 0
    
    for i in range(len(cadenaSpilt)):
        if cadenaSpilt[i] == palabraVieja:
            cadenaSpilt[i] = palabraNueva
            num_reemplazos += 1
    
    cadenaNueva = " ".join(cadenaSpilt)
    
    return cadenaSpilt , num_reemplazos

cadena = "Hola como andas pinche Hola  Hola pendejo perro asquereso puto Hola Hola"
palabraBorrar = "Hola"
palabraNueva = "Puto"
cadenaNueva , cantidadBorradas = cambioDePalabras(cadena,palabraBorrar,palabraNueva)
print("Esta en la nueva cadena con la palabra borrada: ", cadenaNueva ,  " y la cantidad de veces que fue reemplazada fue de: ",cantidadBorradas, " veces!!")
        