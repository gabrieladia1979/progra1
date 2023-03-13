def fechas (a,b,c):
    
    fecha = True
    if a<0 or a>30:
        fecha =False
    if b<0 or b>12:
        fecha =False
    if c<0 or c>2023:
        fecha = False
    return fecha

dia=int(input("Ingrese un dia del mes:"))   
mes=int(input("Ingrese un mes:"))
año=int(input("Ingrese un año:"))

if fechas(dia,mes,año) == True:
    print("La fecha es correcta")
else:
    print("La fecha no es correcta")