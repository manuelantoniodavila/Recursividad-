#1.	Una función recursiva que imprima de forma inversa una cadena de caracteres.  

def ImprimirLaCadena(cadena):
    if len(cadena) == 0:
        return ""
    else:
        return cadena [-1] + ImprimirLaCadena (cadena [:-1])
    
dato = input ("Ingrese Texto ")
Cadena_Inversa =ImprimirLaCadena(dato)
print("Imprimir la Cadena: ", Cadena_Inversa)
