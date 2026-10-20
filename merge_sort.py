def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    mijloc = len(lista) // 2
    stanga = merge_sort(lista[:mijloc])
    dreapta = merge_sort(lista[mijloc:])

    rezultat = []
    i = j = 0

    while i < len(stanga) and j < len(dreapta):
        if stanga[i] <= dreapta[j]:
            rezultat.append(stanga[i])
            i += 1
        else:
            rezultat.append(dreapta[j])
            j += 1

    rezultat.extend(stanga[i:])
    rezultat.extend(dreapta[j:])

    return rezultat


numere = [38, 12, 27, 43, 9, 31, 18, 25]

print("Lista initiala:", numere)
print("Lista sortata:", merge_sort(numere))