def selection_sort(lista):
    n = len(lista)
    for i in range(n - 1):
        # Cauta cel mai mic element din partea nesortata
        minim = i
        for j in range(i + 1, n):
            if lista[j] < lista[minim]:
                minim = j
        lista[i], lista[minim] = lista[minim], lista[i]
    return lista


if __name__ == "__main__":
    numere = [64, 25, 12, 22, 11]
    print("Inainte:", numere)
    print("Dupa:   ", selection_sort(numere))
