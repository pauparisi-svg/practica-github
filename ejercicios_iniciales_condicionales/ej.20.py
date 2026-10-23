'''20. A partir del ejercicio anterior, forzar que el usuario solo pueda introducir por teclados 
números entre 0 y 10'''
var_1 = float(input("introuzca un valor de entre 0 y 10: "))
var_2 = float(input("introuzca un valor de entre 0 y 10: "))
if 0<var_1 or var_2>10:
    if var_1>var_2:
          print ("El número",var_1,"es mayor que el número",var_2,)    
    elif var_2>var_1:
            print ("El número",var_2,"es mayor que el número",var_1,)
    elif var_1==var_2:
        print("Ambos números son iguales ")  
else:
    print("Uno o los dos números están fuera de los límites establecidos")

