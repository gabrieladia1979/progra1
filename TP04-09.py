"""TP04-09 | FUNCIÓN ELIMINAR SUBCADENA
Escribir una función para eliminar una subcadena de una cadena de caracteres, a partir de una posición y cantidad de caracteres dadas, devolviendo la cadena resultante. Escribir también un programa para verificar el comportamiento de la misma. Escribir una función para cada uno de los siguientes casos:
A. Utilizando rebanadas
B. Sin utilizar rebanadas"""

def eliminarRebanadas(cad,posc,cant):
    
    cadNueva = cad.lower()
    cadResultantate = cadNueva[:posc] + cadNueva[posc+cant:]
    
    return cadResultantate

def eliminarSinRebanadas(cad,posc,cant):
    nuevaCadena = ""
    for i in range(len(cad)):
        if i < posc or i >= posc + cant:
            nuevaCadena += cad[i]
    return nuevaCadena
        
cad = "Hola que tal muy buenas gente del señor"
print(cad)
posc = 5
cant = 9
print(eliminarRebanadas(cad,posc,cant))
print(eliminarSinRebanadas(cad,posc,cant))