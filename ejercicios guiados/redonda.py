import math
radio = float(input("introduce el radio: "))
area = math.pi*radio**2
longitud = 2*math.pi*radio
print(area)
print(longitud)
"""1. redondear con los dos metodos que aprendimos la semana pasada
   2. dos metodos que incluyen la libreria math
   3. practicar los dos prints
PRIMER METODO DE REDONDEO"""
radio = float(input("introduce el radio: "))
area = math.pi*radio**2
longitud = 2*math.pi*radio
print(round("area,2"))
print(round("longitud,2"))
#SEGUNDO METODO
radio = float(input("introduce el radio: "))
area = math.pi*radio**2
longitud = 2*math.pi*radio
print(f"{area:.2f}")
print(f"{longitud:.2f}")
#METODO DE LIBRERIA 
print(math.ceil(area))
print(math.floor (area))
