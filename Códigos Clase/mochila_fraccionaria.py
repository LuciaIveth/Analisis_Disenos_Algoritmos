import time
import matplotlib.pyplot as plt

def mochila_fraccionaria(capacidad, objetos):
    objetos.sort(key=lambda x: x[0]/x[1], reverse = True)
    total_objetos = 0.0
    mochila = []
    for valor, peso in objetos:
        #Si el objeto se puede guardar completo
        if capacidad >= peso:
            mochila.append((valor,peso))
            total_objetos += valor
            capacidad -= peso

        #El objeto pesa mpas de la capacidad de la mochila
        else: 
            fracc = capacidad / peso
            mochila.append((valor*fracc, peso*fracc))
            total_objetos += valor*fracc
            break

    return total_objetos, mochila

if __name__ == '__main__':
    tiempos = []
    objetos1 = [(5643453,13564354),(13452356,157967997),(18973566090,83569874),(33545566,1584664695)]
    capacidad1 = 3555664
    inicio = time.time()
    total_objetos1, mochila1 = mochila_fraccionaria(capacidad1, objetos1)
    fin = time.time()
    ejecucion = fin - inicio
    tiempos.append	(ejecucion)
    print(f'El total de objetos 1 es {total_objetos1} y la mochila 1 quedó {mochila1}')
    
    objetos2 = [(2958438,4000),(1000,5000),(4000,8000),(3000,9000)]
    capacidad2 = 20000
    inicio = time.time()
    total_objetos2, mochila2 = mochila_fraccionaria(capacidad2, objetos2)
    fin = time.time()
    ejecucion = fin - inicio
    tiempos.append	(ejecucion)
    print(f'El total de objetos 2 es {total_objetos2} y la mochila 2 quedó {mochila2}')
    
    objetos3 = [(5000,23000),(2000,3000),(1000,6000)]
    capacidad3 = 29000
    inicio = time.time()
    total_objetos3, mochila3 = mochila_fraccionaria(capacidad3, objetos3)
    fin = time.time()
    ejecucion = fin - inicio
    tiempos.append	(ejecucion)
    print(f'El total de objetos 3 es {total_objetos3} y la mochila 3 quedó {mochila3}')
    
    objetos4 = [(7000,23000),(2000,4000),(1000,8000),(1000,15000),(3000,1000),(1000,3000)]
    capacidad4 = 55000
    inicio = time.time()
    total_objetos4, mochila4 = mochila_fraccionaria(capacidad4, objetos4)
    fin = time.time()
    ejecucion = fin - inicio
    tiempos.append	(ejecucion)
    print(f'El total de objetos 4 es {total_objetos4} y la mochila 4 quedó {mochila4}')
    
    objetos5 = [(1000,6000),(1000,8000),(1000,10000)]
    capacidad5 = 12000
    inicio = time.time()
    total_objetos5, mochila5 = mochila_fraccionaria(capacidad5, objetos5)
    fin = time.time()
    ejecucion = fin - inicio
    tiempos.append	(ejecucion)
    print(f'El total de objetos 5  es {total_objetos5} y la mochila 5 quedó {mochila5}')
    
    objetos6 = [(3000,11000),(1000,5000),(2000,6000),(3000,4000)]
    capacidad6 = 7000
    inicio = time.time()
    total_objetos6, mochila6 = mochila_fraccionaria(capacidad6, objetos6)
    fin = time.time()
    ejecucion = fin - inicio
    tiempos.append	(ejecucion)
    print(f'El total de objetos 6 es {total_objetos6} y la mochila 6 quedó {mochila6}')
    
    objetos7 = [(1000,1000),(1000,11000),(2000,7000),(3000,25000),(6000,13000)]
    capacidad7 = 39000
    inicio = time.time()
    total_objetos7, mochila7 = mochila_fraccionaria(capacidad7, objetos7)
    fin = time.time()
    ejecucion = fin - inicio
    tiempos.append	(ejecucion)
    print(f'El total de objetos 7 es {total_objetos7} y la mochila 7 quedó {mochila7}')
    
    objetos8 = [(1000,2000),(2000,4000),(3000,6000),(4000,8000)]
    capacidad8 = 16000
    inicio = time.time()
    total_objetos8, mochila8 = mochila_fraccionaria(capacidad8, objetos8)
    fin = time.time()
    ejecucion = fin - inicio
    tiempos.append	(ejecucion)
    print(f'El total de objetos 8 es {total_objetos8} y la mochila 8 quedó {mochila8}')
    
    objetos9 = [(2000,2000),(4000,4000),(6000,6000),(8000,8000),(10000,10000)]
    capacidad9 = 22000
    inicio = time.time()
    total_objetos9, mochila9 = mochila_fraccionaria(capacidad9, objetos9)
    fin = time.time()
    ejecucion = fin - inicio
    tiempos.append	(ejecucion)
    print(f'El total de objetos 9 es {total_objetos9} y la mochila 9 quedó {mochila9}')
    
    objetos10 = [(10000,5000),(12000,15000),(8000,17000),(1000,3000),(1000,1000),(1000,5000),(4000,2000),(1000,13000)]
    capacidad10 = 50000
    inicio = time.time()
    total_objetos10, mochila10 = mochila_fraccionaria(capacidad10, objetos10)
    fin = time.time()
    ejecucion = fin - inicio
    tiempos.append	(ejecucion)
    print(f'El total de objetos 10 es {total_objetos10} y la mochila 10 quedó {mochila10}')
    
    for i in range(10):
        print("Tiempo Arreglos ",tiempos[i])
    
    plt.figure(figsize=(8, 6))
    plt.plot(tiempos, marker='o')
    plt.title("Complejidad de HeapSort")
    plt.xlabel("Tamaño de Entrada")
    plt.ylabel("Tiempo de ejecución")
    plt.grid(True)  
    plt.show()