""" ALguien introduce un numero del 1 al 5.
Ordenador piensa un numero random del 1 al 5
Cuando el usuario acierte el numero se muestra has acertado/ sino Fallaste
EXAMEN """
import random
import sys
num_random_ordenador = random.randint(1,5)
num_jugador = input("introduce un numero del 1 al 5: ")
if num_jugador in "12345":
    if int(num_jugador)==num_random_ordenador:
        print("acertaste")
    else:
        print("fallaste")
else:
    print("NO HAS INTRODUCIDO EL RANGO CORRECTO")

'''if num_jugador>5:
    sys.exit("Has superado el Numero permitido")
if num_jugador==num_random_ordenador:
    print("acertaste")
else:
    print("fallaste")'''