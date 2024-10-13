#Una función recursiva que retorne la suma de los elementos impares del arreglo. 

def LlenarLista(lista, n, i=0):
    if (n==i):
        numero = int(input("Ingrese el numero: "))
        lista.append(numero)
    else:
        numero = int(input("Ingrese el número: "))
        lista.append(numero)  # Agregar el número a la lista
        LlenarLista(lista, n, i + 1)
        
        
def SumaImpares(lista, i):
    if(len (lista))==i:
        return 0
        
    else:
        if (lista[i] %2 !=0):
            return lista[i] + SumaImpares (lista, i+1)
        else:
            return 0 + SumaImpares (lista, i+1)

    
n = int(input("Ingrese la cantidad de elementos a llenar: "))

lista = []
LlenarLista (lista, n, 1)

suma = SumaImpares(lista, 0)

print(f"La suma de los elementos impares es: {suma}")
    