#8.	Una función recursiva que retorne  cuantos ceros hay en un arreglo de enteros.

def ContarCero (lista, indice=0):
    if indice >= len(lista):
        return 0
    
    if lista[indice] == 0:
        return 1 + ContarCero (lista, indice +1 )
    else:
        return ContarCero(lista, indice + 1)
    
arreglos = [8,1,3,5,3,0,1,6,8,4,0,7,4,0,5,0,53,0,2,0,0,5,7,43,0,43,0]
resultado = ContarCero(arreglos)

print(f"La cantidad de ceros en los arreglos es: {resultado}")