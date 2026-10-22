def MergeSort(lista):
    if len(lista) <= 1:
        return lista

    mijloc = len(lista) // 2
    partea_stanga = MergeSort(lista[:mijloc])
    partea_dreapta = MergeSort(lista[mijloc:])

    return Merge(partea_stanga, partea_dreapta)

def Merge(stanga, dreapta):
    rez = []

    while stanga and dreapta:
        if stanga[0] < dreapta[0]:
            rez.append(stanga.pop(0)) #.append adauga elem. la finalul listei | .pop() elimina si retine elem. eliminat
        else:
            rez.append(dreapta.pop(0))

    rez.extend(stanga)
    rez.extend(dreapta)
    
    return rez

lis = [5, 2, 8, 1, 3]
print(MergeSort(lis))

