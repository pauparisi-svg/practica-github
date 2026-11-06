"""23. Modifica el programa anterior para establecer si la nota es un excelente (8.5 a 10), un 
notable (>=6.5 -<8.5), satisfactorio (<6.5 -5) o insuficiente (<5). Controla que la nota 
introducida esté entre 0 y 10. Utilizar elif sin operadores lógicos. """
nota = float(input("Introduce la nota: "))
if nota >= 0 and nota <= 10:
    if nota < 5:
        print(f"Has sacado un {nota} y has suspendido")
    elif nota < 6.5:
        print(f"Has sacado un {nota} y es satisfactorio")
    elif nota < 8.5:
        print(f"Has sacado un {nota} y es notable")
    else:
        print(f"Has sacado un {nota} y es excelente")
else:
    print("La nota que has introducido no está entre 0 y 10")