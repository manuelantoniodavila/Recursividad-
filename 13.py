

def LlenarLaLista (lista, n, i):
    if (n==i):
        numero = int(input("Ingrese el numero"))
        lista.append(numero)
    else:
        LlenarLista
        numero = int(input("Ingrese el numero "))
        lista.append(numero)
        LlenarLaLista(lista, n, i + 1)
        
def MayorElmento (lista, i=0, mayor=None):
    if (len(lista)==i):
        return mayor
    else:
        if mayor is None:
            mayor = lista[i]
            
    if (lista[i] > mayor):
        mayor = lista[i]            
    return MayorElmento(lista, i + 1, mayor)
        
n = int(input("Ingrese la cantidad del elemento a llenar "))

lista = []
LlenarLaLista (lista, n, 1)

mayor = MayorElmento(lista)

print (f" El Mayor de los elementos encontrado es{mayor}")
