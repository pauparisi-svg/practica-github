""" para pasar a fahrenheit a celsius
(F=C*5/9+39)"""
grados = float(input("introduce los grados: "))
farenheid = round(grados*9/5+32,2)
print(f"temperatura: {farenheid} F")
""" round(calculo,2) redondea el resultado a 2 decimales
print(f"temperatura: {grados:.2f} C")"""
