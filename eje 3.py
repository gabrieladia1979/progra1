def descuento(a):
    valor = 25
    if a > 1 and a <= 20:
        montoTotal = valor * a
    elif a > 20 and a <= 30:
        montoTotal = valor * a
        a = a - 20
        montoTotal = montoTotal + a * (valor-(valor*0.2))
    elif a > 30 and a <= 40:
        montoTotal = valor * a
        a = a - 20
        montoTotal = montoTotal + a * (valor-(valor*0.2))
        a = a - 10
        montoTotal = montoTotal + a * (valor-(valor*0.3))
    elif a >=40:
        montoTotal = valor * a
        a = a - 20
        montoTotal = montoTotal + a * (valor-(valor*0.2))
        a = a - 10
        montoTotal = montoTotal + a * (valor-(valor*0.3))
        a = a - 10
        montoTotal = montoTotal + a * (valor-(valor*0.4))
    return montoTotal

cantidadDeViajes = int(input("Ingrese la cantidad de viajes al mes:"))
while cantidadDeViajes < 1:
    cantidadDeViajes = int(input("Ingrese la cantidad de vaijes correcta:"))

print(descuento(cantidadDeViajes))
