def InsertionSort(lista):
    for i in range(1, len(lista)):
        element = lista[i]
        j = i - 1

        while j >= 0 and lista[j] > element:
            lista[j + 1] = lista[j]
            j = j - 1
        lista[j + 1] = element
    return lista

a = [5, 2, 8, 1, 3]
print(InsertionSort(a))  