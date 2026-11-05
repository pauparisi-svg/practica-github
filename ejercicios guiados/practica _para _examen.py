import random 
ordenador = random.randint(1,5)
jugador = input("dime un número entero de entre 1 a 5: ")
if jugador in"12345":
    if int(jugador)==(ordenador):
        print("acertaste")
    else:
        print("fallaste")
else:
    print(" has introducido un número fuera de los pedido")