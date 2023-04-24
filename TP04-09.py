"""TP04-09 | FUNCIÓN ELIMINAR SUBCADENA
Escribir  una  función  para eliminar  una  subcadena  de  una  cadena  de  caracteres,
apartir  de  una  posición  y cantidad  de caracteres dadas, devolviendo la cadena resultante.

Escribir también un programa para verificar el comportamiento de la misma.

Escribir una función para cada uno de los siguientes casos:

A.Utilizando rebanadas
B.Sin utilizar rebanadas"""


def main():
    cad = str(input("Ingresar un cadena cualquiera de caracteres: "))
    posicion = int(input("Ingresar la posicion por donde quiere empezar: "))
    cantidad = int(input("Ingresar cantidad  de caracteres dadas: "))
    
    return cad,posicion,cantidad

def rebanadas(cad,posicion,cantidad): 
    cadRebanada = cad[posicion:cantidad + posicion]
    
    return cadRebanada

def noRebanadas(cadena,posicion,cantidad):
    subcadena = ""
    for i in range(len(cadena)):
        if i >= posicion and i <(posicion+cantidad):
            subcadena = subcadena + cadena[i]
            
    return subcadena
            

cadena , posc , cant = main()
print(rebanadas(cadena,posc,cant))
print(noRebanadas(cadena,posc,cant))