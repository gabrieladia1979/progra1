def mayor (a,b,c):
    lista=[a,b,c]
    may=a
    
    if a==b and b==c:
        return ("No hay un valor mayor estricto, son todos iguales")
    else:
        for i in range(len(lista)):
            if may < lista[i]:
                may=lista[i]
        return may
        
num=int(input("Ingrese un numero:"))
while num < 0:
         num=int(input("Ingrese un numero positivo"))
                 
num2=int(input("Ingrese un numero"))
while num2 < 0:
         num2=int(input("Ingrese un numero positivo"))
                 
num3=int(input("Ingrese un numero"))
while num3 < 0:
         num3=int(input("Ingrese un numero positivo"))
                 
print(mayor(num,num2,num3))
