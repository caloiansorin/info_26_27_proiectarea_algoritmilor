def quick_sort(lista):
    if len(lista) <= 1:                  # 0 sau 1 elemente: e deja sortata
        return lista

    pivot = lista.pop(len(lista) // 2)   # scoatem pivotul din mijlocul listei

    mici = []
    mari = []
    for x in lista:                      # luam pe rand elementele ramase
        if x < pivot:
            mici.append(x)               # mai mic: merge in stanga
        else:
            mari.append(x)               # mai mare sau egal: merge in dreapta

    return quick_sort(mici) + [pivot] + quick_sort(mari)


print(quick_sort([10, 7, 8, 9, 1, 5]))   # [1, 5, 7, 8, 9, 10]
