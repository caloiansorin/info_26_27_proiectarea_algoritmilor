def quickSort(lista):
    if len(lista) <= 1:
        return lista
    
    pivot = lista[len(lista) -1]

    parteaStanga = []
    parteaDreapta = []

    for i in range(0, len(lista) - 1):
        if lista[i] < pivot:
            parteaStanga.append(lista[i])
        else:
            parteaDreapta.append(lista[i])

    # quickSort(parteaStanga)
    # quickSort(parteaDreapta)

    return quickSort(parteaStanga) + [pivot] + quickSort(parteaDreapta)

lista = [5, 4, 3, 2, 2, 1]
print(quickSort(lista))