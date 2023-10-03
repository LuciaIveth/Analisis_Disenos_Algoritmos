#Examen Parcial 01
#Lucia Iveth De La Vega Hernández
#3CM2 Analisis Diseño Algoritmos
#Ordenamiento Burbuja Iterativo

import array
Arreglo = []
Aux = 0

def OrdBurbIter(Arreglo):
    PosUlt = False
    while PosUlt == False:
        PosUlt = True
        for i in range(0,n-1):      
            if Arreglo[i] > Arreglo[i+1]:
                Aux = Arreglo[i]
                Arreglo[i] = Arreglo[i+1]
                Arreglo[i+1] = Aux
                PosUlt = False
    print("Arreglo Ordenado por Burbuja (Iterativo):")
    print(Arreglo)
 
print("Ingrese la cantidad de elementos que contiene el arrelgo: ")
n = int(input())

i=0
while i < n:
    print("Ingrese el elemento ",i+1, ": ")
    AgrElem= int(input())
    Arreglo.append(AgrElem)
    i+=1 

print("Arreglo Inicial:\n",Arreglo)
OrdBurbIter(Arreglo)
    
