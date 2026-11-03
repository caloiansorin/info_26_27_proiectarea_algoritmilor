def countingSort(lista):
    if len(lista) <=1:
        return lista

    minimum = lista[0]
    maximum = lista[0]
    for i in range(len(lista)):
        if minimum > lista[i]:
            minimum = lista[i]
        if maximum < lista[i]:
            maximum = lista[i]
    k = maximum - minimum + 1

    count = []
    for i in range(k):
        count.append(0)
        
    for i in range(len(lista)):
        count[lista[i] - minimum] += 1


    rezultat = []
    for l in range(k):
        for g in range(count[l]):
            rezultat.append(l + minimum)


    return rezultat

lista = [4, 2, 2, 8, 3, 3, 1]

print(countingSort(lista))