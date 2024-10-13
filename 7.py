
def DevuelveElIndice (lista, dato, indice=0):            
    if indice >= len(lista):
        return -1
    
    if lista[indice] == dato:
        return indice
    return DevuelveElIndice(lista, dato, indice + 1)

lista = [10, 20, 30,40 ,50]
dato = 30
resultado = DevuelveElIndice (lista, dato)

if resultado != -1:
    print(f"El número de {dato} se encuentra en {resultado}")
else:
    print(f"El número de {dato} NO se encuentra en la lista")
    
