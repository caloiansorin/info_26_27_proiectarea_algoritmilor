def heap_sort(lista):
    lista = lista.copy()
    n = len(lista)

    def heapify(n, i):
        cel_mai_mare = i
        stanga = 2 * i + 1
        dreapta = 2 * i + 2

        if stanga < n and lista[stanga] > lista[cel_mai_mare]:
            cel_mai_mare = stanga

        if dreapta < n and lista[dreapta] > lista[cel_mai_mare]:
            cel_mai_mare = dreapta

        if cel_mai_mare != i:
            lista[i], lista[cel_mai_mare] = (
                lista[cel_mai_mare],
                lista[i],
            )
            heapify(n, cel_mai_mare)

    # Construim max-heap-ul.
    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)

    # Mutam maximul la sfarsitul listei.
    for i in range(n - 1, 0, -1):
        lista[0], lista[i] = lista[i], lista[0]
        heapify(i, 0)

    return lista


numere = [12, 11, 13, 5, 6, 7, 2, 20]

print("Lista initiala:", numere)
print("Lista sortata:", heap_sort(numere))