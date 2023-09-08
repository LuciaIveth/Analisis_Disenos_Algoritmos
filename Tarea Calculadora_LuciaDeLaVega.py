#Lucia Iveth De La Vega Hernández 3CM2
#Tarea Código Calculadora 

import time #Librería para el tiempo

print('\n********MENÚ CALCULADORA********')
print('\n**1.......................Suma**')
print('\n**2......................Resta**')
print('\n**3.............Multiplicación**')
print('\n**4...................División**')
print('\n********************************')
print('\nElija la opción de la operación que desea hacer: ')
Opc = int(input())

if Opc == 1:
    I = time.time()
    print('\n Ingrese el primer número: ')
    Num1 = float(input())
    print('\n Ingrese el segundo número: ')
    Num2 = float(input())
    Suma = Num1 + Num2
    print('La suma es: ',Suma)
    print('\n')
    F = time.time()
    TE = F - I
    print('Tiempo:',TE)
    
if Opc == 2:
    I = time.time()
    print('\n Ingrese el primer número: ')
    Num1 = float(input())
    print('\n Ingrese el segundo número: ')
    Num2 = float(input())
    Resta = Num1 - Num2
    print('La resta es: ',Resta)
    print('\n')
    F = time.time()
    TE = F - I
    print('Tiempo:',TE)

if Opc == 3:
    I = time.time()
    print('\n Ingrese el primer número: ')
    Num1 = float(input())
    print('\n Ingrese el segundo número: ')
    Num2 = float(input())
    Mult = Num1 * Num2
    print('La multiplición es: ',Mult)
    print('\n')
    F = time.time()
    TE = F - I
    print('Tiempo:',TE)
    
if Opc == 4:
    I = time.time()
    print('\n Ingrese el primer número: ')
    Num1 = float(input())
    print('\n Ingrese el segundo número: ')
    Num2 = float(input())
    Div = Num1 / Num2
    print('La división es: ',Div)
    print('\n')
    F = time.time()
    TE = F - I
    print('Tiempo:',TE)


