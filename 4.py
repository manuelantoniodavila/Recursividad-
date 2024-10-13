#4.	Una función recursiva que retorne cuantas palabras tienen una frase.
def ContarLasPalabras (cadena):
    if len(cadena) == 0:
        return 0
    else:
        if cadena [0] == '':
            return ContarLasPalabras(cadena[1:])
        else: 
            return 1 + ContarLasPalabras(cadena[1:])
    
cadena = input("Ingrese Texto: ")
contar = ContarLasPalabras(cadena)

print (f"La Frase contiene {contar} palabras")

