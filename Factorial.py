# Funcion Recursiva
def FactorialN(n):
    if(n == 1): # Donde Finaliza
        return n
    
    else: # Llamado Recursivo
        return n * FactorialN(n-1)

# Ejecucion principal del programa
n = int(input("Ingrese el numero que sea saber su factorial: "))

# Ejecucion de Funcion Recursiva
factorial = FactorialN(n) # Donde Inicia

# Resultado
print(f"Factorial es: {factorial}")

