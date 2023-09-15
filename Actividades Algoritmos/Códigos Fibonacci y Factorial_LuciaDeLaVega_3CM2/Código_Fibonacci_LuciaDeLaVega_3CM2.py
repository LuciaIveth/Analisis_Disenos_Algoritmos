#Lucia Iveth De La Vega Hernández
#3CM2 Código Fibonacci

print('Ingrese la posición del número: ')
PNum = int(input())

fibo = [1,1]

for i in range(2, PNum+1):
    fibo.append(fibo[i-2] + fibo[i-1])
print('El número en la posición ', PNum, ' es ', fibo[PNum])