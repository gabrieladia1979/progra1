"""TP04-08 | FUNCIÓN TOMAR SUBCADENA
Desarrollar una función que extraiga una subcadena de una cadena de caracteres,
indicando la posición y la cantidad de caracteres deseada.

Devolver la subcadena como valor de retorno. Escribir también un programa para verificar el comportamiento de la misma.
Ejemplo, dada la cadena "El número de teléfono es 4356-7890"
extraer la subcadena que comienza en la posición 25 y tiene 9 caracteres, resultando la subcadena "4356-7890".
Escribir una función para cada uno de los siguientes casos:

A. Utilizando rebanadas
B. Sin utilizar rebanadas"""

def extraerCadenaRebanada(cadena,posicion,cantidad):
    extraccion = cadena[posicion:posicion + cantidad]
    
    return extraccion

def extraerCadenaSinRebanada(cadena,posicion,cantidad):
    cadenaNueva = ""
    for i in range(cantidad):
        cadenaNueva += cadena[posicion + i] #La posicion de una cadena va del 1 al len(lista)-1
    
    return cadenaNueva
        
    

cadena = input("Ingresar una cadena: ")
posicion = int(input("Ingresar una posicion: "))
cantidad = int(input("Ingresar una cantidad de caracteres quiere extraer: "))

print(extraerCadenaRebanada(cadena,posicion,cantidad))
print(extraerCadenaSinRebanada(cadena,posicion,cantidad))
    
