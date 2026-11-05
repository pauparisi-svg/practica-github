res = input("introuduce una letra ")
"""isalfa: detectar letras-isnumeric: detectar numeros"""
if res.isnumeric()==False:
    if res.isupper() == True:
        print("es mayuscula")
    else: 
        print(" es minuscula")
else:
    print("el valor introducido no es una letra ")