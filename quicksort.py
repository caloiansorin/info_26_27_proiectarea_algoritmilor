def quick_sort(lista):
    if len(lista) <= 1:
        return lista

    pivot = lista[0]

    stanga = []
    dreapta = []

    for i in range(1, len(lista)):
        if lista[i] < pivot:
            stanga.append(lista[i])
        else:
            dreapta.append(lista[i])

    return quick_sort(stanga) + [pivot] + quick_sort(dreapta)


lista = [5, 2, 4, 1]
print(quick_sort(lista))