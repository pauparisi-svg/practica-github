"""31. Asigna a una variable de texto la siguiente frase: A quién madruga Dios ayuda.
Comprueba si existen las siguientes palabras mostrando por pantalla la posición de su
índice."""
frase = "A quién madruga Dios ayuda."
frase = frase.lower()
if "madruga" in frase:
    print("La palabra está en la frase y está en el índice", frase.find("madruga"))
else:
    print("La palabra no está en la frase")

if "dios" in frase:
    print("La palabra está en la frase y está en el índice", frase.find("dios"))
else:
    print("La palabra no está en la frase")

if "dios" in frase:
    print("La palabra está en la frase y está en el índice", frase.find("dios"))
else:
    print("La palabra no está en la frase")