"""TP04-13 | BARAJA ESPAÑOLA
Escribir un programa para crear mediante listas por comprensión los naipes de la baraja española de 48 cartas.
La lista debe contener cadenas de caracteres. Ejemplo: ["1 de Oros", "2 de Oros"... ].
Imprimir la lista por pantalla.
(investigar en internet el tema “python listas por comprensión producto cartesiano de dos listas”)"""

numeros = [str(i) for i in range(1,13)]

cartas = ["Oro","Palo","Espada","Copa"]

nuevaCadena = [numero + " de " + carta for carta in cartas for numero in numeros]


print(nuevaCadena)

"""
for i,carta in enumerate(cartas):
    for j,numero in enumerate(numeros):
        nuevaCadena.append(numero + " de " + carta)
        
        [[nuevaCadena.append(numero + " de " + carta) for numero in numeros] for carta in cartas]

"""
    