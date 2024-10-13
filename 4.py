#4.	Una función recursiva que retorne cuantas palabras tienen una frase.
def ContarPalabras (cadena):
    if len(cadena) == 0:
        return 0
    else:
        if cadena [0] == '':
            return ContarPalabras(cadena[1:])
        else: 
            return 1 + ContarPalabras(cadena[1:])
    
cadena = input("Ingrese un Texto: ")
contar = ContarPalabras(cadena)

print (f"La Frase tiene {contar} palabras")

