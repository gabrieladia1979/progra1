"""Desarrollar un programa que pida un valor de minuto, y un valor de segundo. A partir de esos valores mostrar un reloj
digital en formato de display MM:SS (cada valor siempre en 2 dígitos). El display deberá ir en cuenta regresiva cada 1
segundo hasta llegar a 00:00. Cuando llegue a cero deberá detenerse y mostrar el mensaje “<<<< TIEMPO >>>>"""
import time

def reloj(minutos,segundos):
    final = (f"{minutos:02d}:{segundos:02d}")
    return final

minutos = int(input("Ingrese el minuto para el temporizador: "))
segundos = int(input("Ingrese el segundos para el temporizador: ")) 

while True:
    
    segundos = segundos - 1
    
    if minutos == 0 and segundos == 0:
        print("<<<<TIEMPO>>>>")
        exit()
        
    if segundos  == 0:
        segundos = 60
        minutos = minutos - 1
    
    
    
    print(reloj(minutos,segundos))
    
    time.sleep(1)

    
    
