

def LlenarLaLista(lista, n, i=0):
    if (n==i):
        numero = int(input("Ingrese los numeros"))
        lista.append(numero)
    else:
        numero = int(input("Ingrese los número"))
        lista.append(numero)  # Agregar el número a la lista
        LlenarLaLista(lista, n, i + 1)
        
def SumaDeLongitudes(lista, i ):
    if(len(lista))== i:
        return 0
    
    else:
        return lista[i] + SumaDeLongitudes (lista, i+1)
    
    
n = int(input("Ingrese la cantidad de elementos a ingresar "))

lista = []
LlenarLaLista (lista, n, 1)

suma = SumaDeLongitudes(lista, 0)

print(f" La suma de las longitudes de las cadenas de caracteres es: {suma}")

    
