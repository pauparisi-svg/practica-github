"""27. Mejora el programa anterior para controlar que el valor introducido es una letra y en
caso de introducir un número, aparezca un aviso por pantalla """
letra = input("Dígame una letra: ")

if letra.isalpha():
    mayuscula = letra.isupper()

    if mayuscula == True:
        print("La letra es mayúscula")

    if mayuscula == False:
        print("La letra es minúscula")
if letra.isdigit():
    print("El valor introducido es un número")
else:
    print("El valor introducido es un símbolo")