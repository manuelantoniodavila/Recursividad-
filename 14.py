#Se tiene un arreglo de N  cadenas de caracteres, 
# realice una función recursiva que imprima las 
# cadenas de caracteres que su longitud sea menor a 5

def LlenarLista (lista, n, i= 0):
    if (n==i):
        return
    else:
    
        dato = (input("Ingrese un texto: "))
        lista.append(dato)
        LlenarLista(lista, n, i + 1)
    
    
def ImprimirMenores(lista, i=0):
    if i >= len(lista):
        return
        
    if len(lista[i]) < 5:
        print(lista[i])   
        
        
    ImprimirMenores(lista, i + 1)

        
n = int(input("Ingrese la cantidad de cadena a llenar: "))

lista = []
LlenarLista(lista, n )



print(f"Cadena de caracteres en su longitud menor de 5: ")

Imprimir = ImprimirMenores(lista)