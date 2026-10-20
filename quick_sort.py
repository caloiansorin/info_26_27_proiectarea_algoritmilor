def quick_sort(lista):
    if len(lista) <= 1:
        return lista

    pivot = lista[len(lista) // 2]

    mai_mici = [x for x in lista if x < pivot]
    egale = [x for x in lista if x == pivot]
    mai_mari = [x for x in lista if x > pivot]

    return quick_sort(mai_mici) + egale + quick_sort(mai_mari)


numere = [10, 7, 8, 9, 1, 5, 3, 12]

print("Lista initiala:", numere)
print("Lista sortata:", quick_sort(numere))