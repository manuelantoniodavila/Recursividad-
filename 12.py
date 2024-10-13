 

def LlenarLaLista(lista, n, i):
    if (n==i):
        numero = int(input("Ingrese el numero "))
        lista.append(numero)
    else:
        numero = int(input("Ingrese el número "))
        lista.append(numero)  
        LlenarLaLista(lista, n, i + 1)
        
def SumaDeLosPares(lista, i):
    if (len(lista) == i):
        return 0
    if (lista[i] % 2 == 0):
        return lista[i] + SumaDeLosPares (lista, i+1)
    else:
        return SumaDeLosPares(lista, i+1)
    
n = int(input("Ingresse la cantidad del elemento a llenar"))

lista = []
LlenarLaLista (lista, n, 1)
suma = SumaDeLosPares (lista, 0)


print (f" La Suma de los elementos Pares es: {suma}")
