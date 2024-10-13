#Una función recursiva que retorne el mayor de los 
# elementos de un arreglo de enteros. 

def LlenarLista (lista, n, i):
    if (n==i):
        numero = int(input("Ingrese el numero: "))
        lista.append(numero)
    else:
        LlenarLista
        numero = int(input("Ingrese el numero: "))
        lista.append(numero)
        LlenarLista(lista, n, i + 1)
        
def MayorElmento (lista, i=0, mayor=None):
    if (len(lista)==i):
        return mayor
    else:
        if mayor is None:
            mayor = lista[i]
            
    if (lista[i] > mayor):
        mayor = lista[i]            
    return MayorElmento(lista, i + 1, mayor)
        
n = int(input("Ingrese la cantidad del elemento a llenar: "))

lista = []
LlenarLista (lista, n, 1)

mayor = MayorElmento(lista)

print (f" El Mayor de los elementos es: {mayor}")