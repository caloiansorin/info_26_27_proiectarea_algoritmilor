def selection_sort(lista):
    lista = lista.copy()
    n = len(lista)

    for i in range(n):
        minim = i

        for j in range(i + 1, n):
            if lista[j] < lista[minim]:
                minim = j

        lista[i], lista[minim] = lista[minim], lista[i]

    return lista


numere = [64, 25, 12, 22, 11, 5, 90]

print("Lista initiala:", numere)
print("Lista sortata:", selection_sort(numere))