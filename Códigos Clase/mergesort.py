#Dividir el arreglo en mitades
def MergeSort(Arreglo):
    #CASO BASE
    #Verificar que el arreglo tiene un solo elemento
    if len(Arreglo) <= 1:
        return Arreglo
    #DIVIDIR
    #Obtener la mitad
    Mitad = len(Arreglo)//2  #Doble // para redondear la división para tener entero
    Izq = Arreglo[:Mitad]  #[]Parámetros de dónde a dónde (va desde el inicio del arreglo hasta donde se indique)
    Der = Arreglo[Mitad:]  #[] Si no lleva parámetro significa que va desde donde se indica el arreglo hasta donde termine

    #CONQUISTAR
    Izq = MergeSort(Izq)
    Der = MergeSort(Der)

    #COMBINAR
    #Fusionar las soluciones recursivas
    return Merge(Izq,Der)

def Merge(Izq,Der):
    Ordenado = []
    i_Izq, i_Der =0, 0
    
    #Ciclo para comparar los elementos
    while i_Izq < len(Izq) and i_Der < len(Der):
        if Izq[i_Izq] < Der[i_Der]:
            Ordenado.append(Izq[i_Izq])
            i_Izq += 1
        else:
            Ordenado.append(Der[i_Der])
            i_Der += 1
    
    #Agregar todos los elementos restantes, si existen (Longitud Número Impar)
    Ordenado.extend(Izq[i_Izq:])
    Ordenado.extend(Der[i_Der:])

    return Ordenado

if __name__ == '__main__':
    Arreglo = [4,2,3,1,5,7,6,8,9]
    print('Arreglo desordenado: ',Arreglo)
    Ordenado = MergeSort(Arreglo)
    print('Arreglo ordenado: ',Ordenado)