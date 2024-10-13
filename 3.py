
def ContarLaPalabra (cadena):
    if len(cadena) == 0:
        return ""
     
cadena = input("Ingrese Un Texto: ")
Contar = "Aa"

contardor = sum (1 for char in cadena if char in Contar)

print (f" El Total de a encontrado es{contardor}")
