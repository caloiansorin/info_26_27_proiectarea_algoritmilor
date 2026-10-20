def insertion_sort(lista):
    for i in range(1, len(lista)):
        cheie = lista[i]
        j = i - 1
        # Muta elementele mai mari cu o pozitie la dreapta
        while j >= 0 and lista[j] > cheie:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = cheie
    return lista


if __name__ == "__main__":
    numere = [64, 25, 12, 22, 11]
    print("Inainte:", numere)
    print("Dupa:   ", insertion_sort(numere))
