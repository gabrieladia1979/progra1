"""
-----------------------------------------------------------------------------------------------
Título:
Fecha:
Autor:
Descripción:
-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS IMPORTADOS
#----------------------------------------------------------------------------------------------
import random

#----------------------------------------------------------------------------------------------
# FUNCIONES

def borrarCadena(cadnombres,cadImporte ):
    cadnombres = []
    cadImporte = []
    return cadnombres , cadImporte

def agregarAmigosAlSorteo(listaDeAmigos , listaDeImportes):

    while True:

        amigo = input("Que amigo agrego a la lista?: ")
        print(amigo)

        if amigo == "fin":
           break

        listaDeAmigos.append(amigo)

        importe = int(input("Que importe suma al pozo acumulado?"))
        listaDeImportes.append(importe)

    return listaDeAmigos , listaDeImportes

def realizarSorteo(cadAmigos , cadImporte):

    pozoAcumulado = 0
    
    #Suma de pozo acumulado
    for i in range(len(cadImporte)):
        
        pozoAcumulado += cadImporte[i]

    porciento1 = (pozoAcumulado*50) / 100
    porciento2 = (pozoAcumulado*30) / 100
    porciento3 = (pozoAcumulado*20) / 100
    
    #Los 3 primeros ganadores 
    for i in range(1,4):

        nombreRandom = random.choice(cadAmigos)

        if i == 1:
            print(nombreRandom, " es el sorteado número ",i ,"con una ganancia de",porciento1)
        if i == 2:
            print(nombreRandom, " es el sorteado número ",i ,"con una ganancia de",porciento2)
        if i == 3:
            print(nombreRandom, " es el sorteado número ",i ,"con una ganancia de",porciento3)
            
        cadAmigos.remove(nombreRandom)
    
    cadLimpia1 , cadLimpia2 = borrarCadena(cadAmigos,cadImporte )
    
    return cadLimpia1 , cadLimpia2

def subirApuesta(cadAmigos,cadImporte):
    
    for i,amigo in enumerate(cadAmigos):
        print("ID ",i+1," - ",amigo," aposto ",cadImporte[i])
        print("")
        print("")
    
    persona = input("Seleccione el ID de la persona que quiere modificar el importe: ")
        
    for i in range(len(cadAmigos)):
        
        if cadAmigos[i] == persona:
            
            nuevoImp = int(input("Que importe nuevo quiere introducirle: "))
            cadImporte[i] == nuevoImp
            print("Importe modificado con exito . . . volviendo al menu")
            return cadAmigos , cadImporte
        
    

#----------------------------------------------------------------------------------------------
...

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
# Declaración de variables
listaDeAmigos , listaDeImportes = [] , []
#----------------------------------------------------------------------------------------------
...

# Bloque de menú
#----------------------------------------------------------------------------------------------
while True:
    while True:
        print()
        print("---------------------------")
        print("MENÚ DEL SISTEMA           ")
        print("---------------------------")
        print("[1] Cargar Amigos al sorteo")
        print("[2] Sortear!")
        print("[3] Vaciar lista de amigos")
        print("[4] Subir la apuesta!")
        print("[0] Salir del programa")
        print()
        opcion = int(input("Seleccione una opción: "))
        if opcion in range(0,5): # Sólo continua si se elije una opcion de menú válida
            break

    if opcion == 0: # Opción salir del programa
        exit()

    elif opcion == 1:   # Opción Cargar Amigos al sorteo
        
         agregarAmigosAlSorteo(listaDeAmigos , listaDeImportes)
        
    elif opcion == 2:   # Sortear!
        
        realizarSorteo(listaDeAmigos , listaDeImportes)
        
    elif opcion == 3:   # Vaciar lista de amigos
        
        borrarCadena(listaDeAmigos, listaDeImportes)
        
    elif opcion == 4:   # Subir la apuesta!
       subirApuesta(listaDeAmigos,listaDeImportes)

    print()
    input("Presione ENTER para continuar.")

