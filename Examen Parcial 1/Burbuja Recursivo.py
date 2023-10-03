#Examen Parcial 01
#Lucia Iveth De La Vega Hernández
#3CM2 Analisis Diseño Algoritmos
#Ordenamiento Burbuja Recursivo

import array
Arreglo = []
Aux = 0
PosUlt = False

def OrdBurbRecu(Arreglo,i,PosUlt,n):

    while PosUlt == False:
        PosUlt = True
        if (Arreglo[i] > Arreglo[i+1])&(i<n):
            print("Entra if")
            Aux = Arreglo[i]
            Arreglo[i] = Arreglo[i+1]
            Arreglo[i+1] = Aux
            PosUlt = False
            i+=1
            print(Arreglo)
            return OrdBurbRecu(Arreglo,i,PosUlt,n)
        else:
            i=0
            return OrdBurbRecu(Arreglo,i,PosUlt,n)
    print("Arreglo Ordenado por Burbuja (Recursivo):")
    print(Arreglo)      
  

print("Ingrese la cantidad de elementos que contiene el arrelgo: ")
n = int(input())

i=0
while i < n:
    print("Ingrese el elemento ",i+1, ": ")
    AgrElem= int(input())
    Arreglo.append(AgrElem)
    i+=1 

i=0
print("Arreglo Inicial:\n",Arreglo)
OrdBurbRecu(Arreglo,i,PosUlt,n)