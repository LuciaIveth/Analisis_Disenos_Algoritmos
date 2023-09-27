#Lucia Iveth De La Vega Hernández
#3CM2 Código Fibonacci Recursivo

def fibo(PNum):
   
   if PNum <= 1:
       return PNum
   
   else:
       return(fibo(PNum-1) + fibo(PNum-2))

print('Ingrese la posición del número: ')
PNum = int(input())

if PNum <= 0:
   print("Ingrese un número positivo para poder realizar el Fibonacci")
else:
      print('El número en la posición ', PNum, ' con Fibonacci es: ',fibo(PNum))