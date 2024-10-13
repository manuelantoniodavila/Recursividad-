#12.Se tiene un arreglo de N elementos de tipo enteros, 
# realice una función recursiva que retorne la suma de
# los elementos almacenado en las casillas pares del 
# arreglo. 

def LlenarLista(lista, n, i):
    if (n==i):
        numero = int(input("Ingrese el numero: "))
        lista.append(numero)
    else:
        numero = int(input("Ingrese el número: "))
        lista.append(numero)  # Agregar el número a la lista
        LlenarLista(lista, n, i + 1)
        
def SumaPare (lista, i):
    if (len(lista) == i):
        return 0
    if (lista[i] % 2 == 0):
        return lista[i] + SumaPare (lista, i+1)
    else:
        return SumaPare(lista, i+1)
    
n = int(input("Ingresse la cantidad del elemento a llenar: "))

lista = []
LlenarLista (lista, n, 1)
suma = SumaPare (lista, 0)


print (f" La Suma de los elementos alamacenados Pares es: {suma}")
