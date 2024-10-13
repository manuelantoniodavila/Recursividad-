 
def ContarLasCadena(cadena):
    if len(cadena) == 0:
        return ""
    
cadena = input ("Ingrese un Texto: ")


contador = 0
vocales = "aeiouAEIOU"

contador += sum(1 for char in cadena if char in vocales)

#for letra in Cadena:
#    if letra in vocales:
#       Contar += 1

print(f"El total de vocales encontradas es {contador}")
