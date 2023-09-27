#Lucia Iveth De La Vega Hernández
#3CM2 Código Factorial Recursivo

def facto(Num):
   if Num <= 1:
       return Num
   
   else:
       return(Num*facto(Num-1))

print('Ingrese el número del que desea su factorial: ')
Num = int(input())

if Num < 0:
   print("Ingrese un número positivo para poder realizar el Factorial")

elif Num == 0 :
    print("Ingrese un número distinto de 0 para poder realizar el Factorial")
    
else:
      print('El Factorial de ', Num, ' es: ',facto(Num))