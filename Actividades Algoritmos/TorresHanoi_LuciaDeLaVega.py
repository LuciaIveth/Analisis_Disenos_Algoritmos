#Lucia Iveth De La Vega Hernández
#3CM2 Código Torres de Hanói Recursivo

def CambTorre(nivel,actual,aux,destino):
    #Caso base
    if nivel == 1:
        print("     Se cambió el disco de la varilla ",actual," hasta la varilla ",destino)
    #Caso General
    else:
        CambTorre(nivel-1,actual,destino,aux)
        print("     Se cambió el disco de la varilla ",actual," hasta la varilla ",destino)
        CambTorre(nivel-1,aux,actual,destino)
        

print("Ingrese el número de discos de la Torre de Hanói: ")
nivel = int(input())

print("\n***Solución de la Torre de Hanói con ",nivel," discos***")
CambTorre(nivel,"A","B","C")