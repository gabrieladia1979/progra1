"""TP04-10 | PALABRAS DE FRASE ORDENADAS
Escribir una función que reciba como parámetro una cadena de caracteres en la que las palabras se encuentran separadas por uno o más espacios.
Devolver otra cadena con las palabras ordenadas alfabéticamente, dejando un espacio entre cada una."""

def ordenar(cadena):
    
    palabras = cadena.split()
    
    ordenarPalabras = sorted(palabras)
    
    cadenaOrdenada =  " ".join(ordenarPalabras)
    
    return cadenaOrdenada

cadena = "hola     como     andas todo bom" #No puede haber mayusculas
print(ordenar(cadena))

