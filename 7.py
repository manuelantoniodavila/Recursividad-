#7.	Realice una función recursiva de búsqueda secuencial, 
# la función devuelve el índice donde se encontró el  elemento buscado. 

def DevuelveIndice (lista, dato, indice=0):            
    if indice >= len(lista):
        return -1
    
    if lista[indice] == dato:
        return indice
    return DevuelveIndice(lista, dato, indice + 1)

lista = [10, 20, 30,40 ,50]
dato = 30
resultado = DevuelveIndice (lista, dato)

if resultado != -1:
    print(f"El número {dato} se encuentra en : {resultado}")
else:
    print(f"El número {dato} NO se encuentra en la lista.")
    