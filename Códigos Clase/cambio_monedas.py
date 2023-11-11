def cambio_monedas(cantidad, denoms):
    sol = []
    total = 0

    #Asegurar que la lista está del más grande al más chico
    denoms.sort(reverse = True)

    for d in denoms:
        #Guarda las monedas hasta que se cumple con el total de cambio
        while total + d <= cantidad:
            sol.append(d)
            total += d
    return sol

if __name__ == '__main__':
    cantidad = 98
    denominaciones = [1, 2, 5, 10]
    sol = cambio_monedas(cantidad, denominaciones)
    print(f'La cantidad {cantidad} necesita {sol} de monedas')