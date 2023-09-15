#Lucia Iveth De La Vega Hernández
#3CM2 Código Factorial

print('Escriba el número que desea obtener su factorial: ')
num= int(input())
factorial=1
k=1

while(k<=num):
        factorial = k*factorial
        k=k+1
print('El factorial de ',num,' es: ')
print(factorial)
