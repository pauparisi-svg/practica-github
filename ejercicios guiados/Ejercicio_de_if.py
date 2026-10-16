""" ALguien introduce un numero del 1 al 5.
Ordenador piensa un numero random del 1 al 5
Cuando el usuario acierte el numero se muestra has acertado/ sino Fallaste """
import random
import sys
num_random_ordenador = random.randint(1,5)
num_jugador = int(input("introduce un numero del 1 al 5: "))

if num_jugador>5:
    sys.exit("Has superadp el Numero permitido")
if num_jugador==num_random_ordenador:
    print("acertaste")
else:
    print("fallaste")