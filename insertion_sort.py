def insertion_sort(lista):
    lista = lista.copy()

    for i in range(1, len(lista)):
        valoare = lista[i]
        j = i - 1

        while j >= 0 and lista[j] > valoare:
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = valoare

    return lista


numere = [8, 4, 6, 2, 9, 1, 5]

print("Lista initiala:", numere)
print("Lista sortata:", insertion_sort(numere))