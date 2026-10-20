def bubble_sort(lista):
    n = len(lista)
    for i in range(n - 1):
        schimbat = False
        for j in range(n - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                schimbat = True
        # Daca nu s-a facut nicio schimbare, lista e deja sortata
        if not schimbat:
            break
    return lista


if __name__ == "__main__":
    numere = [64, 25, 12, 22, 11]
    print("Inainte:", numere)
    print("Dupa:   ", bubble_sort(numere))
