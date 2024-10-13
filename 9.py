#9.	Una función recursiva que retorne la suma de los elementos positivos del arreglo.

def LlenarLista (lista, n, i):
    if (n==i):
        numero = int(input("Ingrese el numero: "))
        lista.append(numero)
    else:
        LlenarLista
        numero = int(input("Ingrese el numero: "))
        lista.append(numero)
        LlenarLista(lista, n, i+1)
        
def SumaPositivo(lista, i):
    if(len (lista) == i):
        return 0
    else:
        if (lista[i] > 0):
            return lista[i] + SumaPositivo (lista, i+1)
        else:
            return 0 + SumaPositivo (lista, i+1)
        
        
#Ejecucion principal del programa
n= int (input("Ingresse la cantidad del elemento a llenar: "))

lista = []
LlenarLista (lista, n, 1)


suma = SumaPositivo(lista, 0)

print(f"La suma positivo es: {suma}")

