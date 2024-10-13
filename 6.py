#6.	Una función recursiva que retorne true o false si la cadena de caracteres es de una palabra.

def UnaPalabra(frase, i):
    
    if(frase[i]==""):
        return False
    
    elif(len(frase)-1==i):
        return True
    else:
        return UnaPalabra(frase, i+1)
        
#Ejecucion principal del programa

frase= input("Ingresse la frase para saber si es una palabra o frase: ")

#Ejecucion de funcion  recursiva
band = UnaPalabra (frase, 0)

if (band):
    print("Es una palabra")
else:
    print("No es una palabra")