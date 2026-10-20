def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    mijloc = len(lista) // 2
    stanga = merge_sort(lista[:mijloc])
    dreapta = merge_sort(lista[mijloc:])

    return interclasare(stanga, dreapta)


def interclasare(stanga, dreapta):
    rezultat = []
    i = j = 0

    while i < len(stanga) and j < len(dreapta):
        if stanga[i] <= dreapta[j]:
            rezultat.append(stanga[i])
            i += 1
        else:
            rezultat.append(dreapta[j])
            j += 1

    # Adauga elementele ramase
    rezultat.extend(stanga[i:])
    rezultat.extend(dreapta[j:])
    return rezultat


if __name__ == "__main__":
    numere = [64, 25, 12, 22, 11]
    print("Inainte:", numere)
    print("Dupa:   ", merge_sort(numere))
