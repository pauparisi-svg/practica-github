"""19. Programa que introduzca dos números y devuelva cuál de los dos es mayor, menor o son 
iguales """
var_1 = float(input("introuzca un valor: "))
var_2 = float(input("introuzca un valor: "))
if var_1>var_2:
    print("El número" ,var_1, "es mayor que el número",var_2,)
elif var_2>var_1:
    print("El número",var_2,"es mayor que el número ",var_1,)
else:
    print("Ambos números son iguales ")