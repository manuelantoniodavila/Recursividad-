
def verificarEimprimir(frase, index=0):
    if index == len(frase):
        print(frase)  
        return
    
    if frase[index].lower() == 'a':
        print("La frase contiene la vocal 'a', no se puede imprimir")
        return
    
    verificarEimprimir(frase, index + 1)

frase = input("Ingrese una frase: ")

verificarEimprimir(frase)
