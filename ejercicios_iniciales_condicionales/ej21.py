""" 21. Programa que calcula una ecuación de segundo grado. Controla que el valor de la raíz 
cuadrada no de un valor negativo"""
import math
a = float(input("Introduce el valor de a: "))
b = float(input("Introduce el valor de b: "))
c = float(input("Introduce el valor de c: "))
operación_de_dentro_de_raíz = b**2 - 4*a*c
if operación_de_dentro_de_raíz < 0:
    print("La raíz no puede ser un valor negativo ")
else:
    x1 = (-b + math.sqrt(operación_de_dentro_de_raíz)) / (2*a)
    x2 = (-b - math.sqrt(operación_de_dentro_de_raíz)) / (2*a)
    print(f"El valor de x1 es: {x1} ")
    print(f"El valor de x2 es: {x2} ")