import time

#Lucia Iveth De La Vega Hernández
# 3CM2 Práctica 03
# Algoritmo de Dijkstra

def Dijkstra(Grafo, Salida):
    
    dist, prev = {}, {}
    GrafResul = []

    for vertice in Grafo:
        dist[vertice] = float("inf")
        prev[vertice] = None
    dist[Salida] = 0

    Q = [vertice for vertice in Grafo]

    while Q:
        u = min(Q, key=dist.get)
        Q.remove(u)
        GrafResul.append(u)

        for vecino in Grafo[u]:
            if vecino in Q and dist[vecino] > dist[u] + Grafo[u][vecino]:
                dist[vecino] = dist[u] + Grafo[u][vecino]
                prev[vecino] = u

    return GrafResul, dist, prev

print("\n------GRAFO 1------\n")
Grafo1 = {
    'a': {'b': 9, 'd': 2},
    'b': {'c': 1, 'e': 1},
    'c': {'b': 1, 'e': 7, 'd': 1, 'g': 6},
    'd': {'c': 1, 'g': 10},
    'e': {'f': 2, 'z': 18},
    'f': {'z': 9},
    'g': {'z': 2},
    'z': {}
}
inicio1 = time.time()
Camino1, Distancia1, previos1 = Dijkstra(Grafo1, 'a')
print(f"***Camino mínimo: \n {Camino1=}")
print(f"\n***Distancia del Grafo: \n {Distancia1=}")
fin1 = time.time()
tiempo_ejecutado1 = fin1 - inicio1
print('\nTiempo 1:',tiempo_ejecutado1)

print("\n------GRAFO 2------\n")
Grafo2 = {
    'a': {'b': 6},
    'b': {'c': 7, 'd': 9},
    'c': {'f': 9},
    'd': {'f': 4, 'e': 3},
    'e': {'z': 7},
    'f': {'z': 5},
    'z': {}
}

inicio2 = time.time()
Camino2, Distancia2, previos2 = Dijkstra(Grafo2, 'a')
print(f"***Camino mínimo: \n {Camino2=}")
print(f"\n***Distancia del Grafo: \n {Distancia2=}")
fin2 = time.time()
tiempo_ejecutado2 = fin2 - inicio2
print('\nTiempo 2:',tiempo_ejecutado2)

print("\n------GRAFO 3------\n")
Grafo3 = {
    'a': {'b': 2, 'c': 4, 'd': 6},
    'b': {'e': 10},
    'c': {'f': 4},
    'd': {'f': 2},
    'e': {'g': 8},
    'f': {'g': 3},
    'g': {'h': 2, 'i': 2},
    'h': {'z': 5},
    'i': {'z': 7},
    'z': {}
}

inicio3 = time.time()
Camino3, Distancia3, previos3 = Dijkstra(Grafo3, 'a')
print(f"***Camino mínimo: \n {Camino3=}")
print(f"\n***Distancia del Grafo: \n {Distancia3=}")
fin3 = time.time()
tiempo_ejecutado3 = fin3 - inicio3
print('\nTiempo 3:',tiempo_ejecutado3)

print("\n------GRAFO 4------\n")
Grafo4 = {
    'a': {'b': 10, 'c': 5},
    'b': {'d': 7, 'e': 3},
    'c': {'e': 1, 'f': 2},
    'd': {'z': 6},
    'e': {'d': 3, 'z': 16},
    'f': {'e': 9},
    'z': {}
}

inicio4 = time.time()
Camino4, Distancia4, previos4 = Dijkstra(Grafo4, 'a')
print(f"***Camino mínimo: \n {Camino4=}")
print(f"\n ***Distancia del Grafo: \n {Distancia4=}")
fin4 = time.time()
tiempo_ejecutado4 = fin4 - inicio4
print('\nTiempo 4:',tiempo_ejecutado4)

print("\n------GRAFO 5------\n")
Grafo5 = {
    'a': {'b': 9, 'c': 19, 'd': 13},
    'b': {'c': 10, 'd': 12},
    'c': {'z': 8},
    'd': {'z': 11},
    'z': {}
}

inicio5 = time.time()
Camino5, Distancia5, previos5 = Dijkstra(Grafo5, 'a')
print(f"***Camino mínimo: \n {Camino5=}")
print(f"\n ***Distancia del Grafo: \n {Distancia5=}")
fin5 = time.time()
tiempo_ejecutado5 = fin5 - inicio5
print('\nTiempo 5:',tiempo_ejecutado5)