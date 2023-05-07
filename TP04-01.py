"""TP04-01 | CADENA CAPICÚA
Desarrollar una función que determine si una cadena de caracteres es capicúa, sin utilizar cadenas auxiliares ni rebanadas.
Escribir además un programa que permita verificar su funcionamiento."""

def capicua(palabra):
    funciona = True
    total = len(palabra) // 2
    for i,letra in enumerate(palabra):
        if palabra[i] != palabra[-(i+1)]:
            funciona = False
            return funciona
        
    return funciona
#Manera rara de verlo , funciona pero es mejor hacerlo con for i in range()            
            
cadena = input("Ingrese una cadena: ")

if capicua(cadena) == True:
    print("La cadena es capicua !!!")
else:
    print("La cadena es no es capicua !!!")
        