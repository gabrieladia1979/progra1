"""Escribir una función filtrarPalabras() que reciba una cadena de caracteres conteniendo una frase y un entero N, y devuelva otra cadena con las palabras que tengan N o más caracteres de la cadena original. Escribir también un programa para verificar el comportamiento de la misma. Hacer tres versiones de la función, para cada uno de los siguientes casos:
A. Utilizando ciclos normales y slicing. Sin utilizar el método split()
B. Utilizando el método split() y ciclos normales
C. Utilizando el método split() y listas por comprensión"""

def filtrarPalabras(frase, n):
    palabras = []
    palabra = ''
    for i in range(len(frase)):
        if frase[i] != ' ':
            palabra += frase[i]
        else:
            if len(palabra) >= n:
                palabras.append(palabra)
            palabra = ''
            
    if len(palabra) >= n: #Ponemos 1 afuera porque no tiene "" en el ultimo lugar
        palabras.append(palabra)
        
    return ' '.join(palabras)

def metodoSlipNormal(frase , n):
    palabras = frase.split()
    palabrasFiltradas = []
    
    for palabra in palabras:
        if len(palabra) >= n:
            palabrasFiltradas.append(palabra)
            
    return ' '.join(palabrasFiltradas)

def filtrarPalabras(frase, n):
    palabras = [palabra for palabra in frase.split() if len(palabra) >= n]
    return ' '.join(palabras)

frase = str(input("Ingrese un frase entre espacios: "))
cantidadDePalabras = int(input("Ingresar la cantidad "))
print(filtrarPalabras(frase,cantidadDePalabras))
print(metodoSlipNormal(frase,cantidadDePalabras))