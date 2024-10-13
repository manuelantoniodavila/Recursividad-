
def LlenarLaLista (lista, n, i= 0):
    if (n==i):
        return
    else:
    
        dato = (input("Ingrese un texto "))
        lista.append(dato)
        LlenarLaLista(lista, n, i + 1)
    
    
def ImprimirLosMenores(lista, i=0):
    if i >= len(lista):
        return
        
    if len(lista[i]) < 5:
        print(lista[i])   
        
        
    ImprimirLosMenores(lista, i + 1)

        
n = int(input("Ingrese la cantidad de cadena a llenar "))

lista = []
LlenarLaLista(lista, n )



print(f"Cadena de caracteres en su longitud menor de 5 son ")

Imprimir = ImprimirLosMenores(lista)
