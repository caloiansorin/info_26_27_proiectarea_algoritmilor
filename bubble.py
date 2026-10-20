def bubble_sort(lista):
    for capat in range(len(lista) - 1):
        schimbat = False

        for pozitie in range(len(lista) - 1 - capat):
            if lista[pozitie] > lista[pozitie + 1]:
                lista[pozitie], lista[pozitie + 1] = (
                    lista[pozitie + 1],
                    lista[pozitie],
                )
                schimbat = True

        if not schimbat:
            break

    return lista


numere = [8, 3, 6, 2, 7, 1, 5]
print("Lista initiala:", numere)
bubble_sort(numere)
print("Lista sortata:", numere)