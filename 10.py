
def LlenarLaLista(lista, n, i=0):
    if (n==i):
        numero = int(input("Ingrese los numeros "))
        lista.append(numero)
    else:
        numero = int(input("Ingrese los números "))
        lista.append(numero)  
        LlenarLaLista(lista, n, i + 1)
        
        
def SumaDeImpares(lista, i):
    if(len (lista))==i:
        return 0
        
    else:
        if (lista[i] %2 !=0):
            return lista[i] + SumaDeImpares (lista, i+1)
        else:
            return 0 + SumaDeImpares (lista, i+1)

    
n = int(input("Ingrese la cantidad de elementos que desea llenar"))

lista = []
LlenarLaLista (lista, n, 1)

suma = SumaDeImpares(lista, 0)

print(f"La suma de los elementos impares es{suma}")
    
