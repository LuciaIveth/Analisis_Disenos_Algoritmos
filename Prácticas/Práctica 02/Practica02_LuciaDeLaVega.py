import random
import time
import matplotlib.pyplot as plt

def quicksort(arr):
    
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = []
    right = []
    for i in range(1, len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
    
    
    return quicksort(left) + [pivot] + quicksort(right)

execution_times = []
arreglo = []

for i in range(100):
    
    length = random.randint(1000, 10000)
    arr = [random.randint(1, 100) for j in range(length)]
    arreglo.append(length)
    start_time = time.time()
    sorted_arr = quicksort(arr)
    end_time = time.time()
    execution_time = end_time - start_time
    print("Tiempo: ",execution_time)
    execution_times.append(execution_time)
    print("Tiempo Arreglo: ",execution_time)
    print(f"Array {i+1}: {sorted_arr}")
    
for i in range(100):
    print("Tiempo Arreglos ",execution_times[i])

for i in range(100):
    print("Tamaño Arreglos ",arreglo[i])

plt.plot(execution_times)
plt.xlabel('Tamaño del arreglo')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.title('Tiempo de ejecución de Quicksort en arreglos aleatorios')
plt.show()