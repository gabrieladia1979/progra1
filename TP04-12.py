"""TP04-12 | VOCALES ARRIBA
Se está desarrollando una importante app para tratamiento de texto y
nos piden que desarrollemos una función para una de las opciones de la app.
La función consiste en poner en mayúscula todas las vocales de una frase,
por ejemplo, si la función recibe el texto “frase de prueba para el nuevo programa de tratamiento de texto”
debe devolver “frAsE dE prUEbA pArA El nUEvO prOgrAmA dE trAtAmIEntO dE tExtO”.
Probar la función desde un programa principal"""

def vocalesEnMayus(cadena):
    resultado = ""
    vocales = ["a","e","i","o","u"]
    
    for letra in cadena:
        if letra.lower() in vocales:
            resultado += letra.upper()
        else:
            resultado += letra
    
    return resultado

cadena = "frase de prueba para el nuevo programa de tratamiento de texto"
print(vocalesEnMayus(cadena))