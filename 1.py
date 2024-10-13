#1.	Una función recursiva que imprima de forma inversa una cadena de caracteres.  

def ImprimirCadena (cadena):
    if len(cadena) == 0:
        return ""
    else:
        return cadena [-1] + ImprimirCadena (cadena [:-1])
    
dato = input ("Ingrese un Texto: ")
Cadena_Inversa =ImprimirCadena(dato)
print("Imprimir Cadena: ", Cadena_Inversa)