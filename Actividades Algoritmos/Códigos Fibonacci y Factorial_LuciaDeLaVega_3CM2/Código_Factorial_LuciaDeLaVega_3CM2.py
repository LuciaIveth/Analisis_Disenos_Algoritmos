#Lucia Iveth De La Vega Hernández
#3CM2 Código Factorial

print('Escriba el número que desea obtener su factorial: ')
numfac= int(input())
fact=1
mul=1

while(mul<=numfac):
        fact = mul*fact
        mul=mul+1
print('El factorial de ',numfac,' es: ')
print(fact)
