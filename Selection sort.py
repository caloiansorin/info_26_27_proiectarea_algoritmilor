def SelectionSort(lista):
    for i in range(0,len(lista)-1):
        minIndex = i

        for j in range(i+1, len(lista)):
            if(lista[j]<lista[minIndex]):
                minIndex = j

        if(minIndex!=i):
            aux = lista[minIndex]
            lista[minIndex] = lista[i]
            lista[i] = aux
    return lista

lista=[5, 4, 3, 2, 1]
print(SelectionSort(lista))