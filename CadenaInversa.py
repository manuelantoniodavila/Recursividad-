# Funcion Recursiva
def ImprimirCadenaInversa(cadena, i):
    if(i == 0): # Donde Finaliza
        print(cadena[i])
    
    else: # Llamado Recursivo
        print(cadena[i])
        ImprimirCadenaInversa(cadena, i-1)
        

# Ejecucion principal del programa
cadena = input("Ingrese cadena a invertir: ")

# Ejecucion de Funcion Recursiva
ImprimirCadenaInversa(cadena, len(cadena)-1)