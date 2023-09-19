#Lucia Iveth De La Vega Hernández
#3CM2 Algoritmos 
#Práctica 01
#Código Ordenamiento Burbuja

import array
import time

def MO_Burbuja(arreglo):
    I = time.time()
    for i in range(n-1):      
        for j in range(n-1-i): 
            if arreglo[j] > arreglo[j+1]:
                arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]
    F = time.time()
    TE = F - I
    print("Arreglo Ordenado por Burbuja: ")
    print(elementos)
    print('Tiempo Ejecución:',TE)
    print('\n')

def MO_BurbujaOpt(arreglo):
    I = time.time()
    for i in range(n-1):
        intercambio = False
 
        for j in range(n-1-i):
            if arreglo[j] > arreglo[j+1] :
                arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]
                intercambio = True
 
        if intercambio == False:
            break
    F = time.time()
    TE = F - I
    print("Arreglo Ordenado por Burbuja Optimizada: ")
    print(elementos)
    print('Tiempo Ejecución:',TE)
    print('\n')

 
print("Ingrese la cantidad de elementos que desea agregar: ")
n = int(input())
elementos = []
    
i=0
    
while i<n:
    print("Ingrese el elemento ",i+1, ": ")
    newelem= int(input())
    elementos.append(newelem)
    i+=1 

print("\n**********MENÚ ORDENAMIENTO***********")
print("**Burbuja..........................1**")
print("**Burbuja Optimizada...............2**")
print("**************************************")
print("\nElija la opción del método de ordenamiento que desea: ")
Opc = int(input())

if Opc == 1:
    MO_Burbuja(elementos)
    
if Opc == 2:
    MO_BurbujaOpt(elementos)

    






