while True:
    while True:
        print()
        print("---------------------------")
        print("MENÚ DEL SISTEMA           ")
        print("---------------------------")
        print("1 - Generar matriz ...")
        print("2 - Ordenar matriz ...")
        print("3 - Intercambiar dos filas ...")
        print("4 – Intercambiar dos columnas ...")
        print("5 – Transponer matriz ...")
        print("6 – Promedio de fila ...")
        print("7 – Porcentaje de impares de columna ...")
        print("8 – Verificación de simetría diagonal principal ...")
        print("9 – Verificación de simetría diagonal secundaria ...")
        print()
        print("Seleccione una opción: ")
        
        opcion = int(input("Seleccione una opción: "))
        if opcion in range(0,9): # Sólo continua si se elije una opcion de menú válida
            break

    if opcion == 0: # Opción salir del programa
        exit()  

    elif opcion == 1: # Opción ...
        matriz = []

        tamaño = int(input("Ingrese el tamaño NxN de la matriz: "))
        for i in range(tamaño):
            x = []
            for j in range(tamaño):
               elemento = int(input("Ingresa un elemento: "))
               x.append(elemento)
            matriz.append(x)
    
        print(matriz)

        input("Presione ENTER para continuar.")
        
    elif opcion == 2:   # Opción ...
        
        for 

        input("Presione ENTER para continuar.")
    elif opcion == 3:   # Opción ...

        input("Presione ENTER para continuar.")