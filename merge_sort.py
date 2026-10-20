def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    mijloc = len(lista) // 2
    stanga = merge_sort(lista[:mijloc])
    dreapta = merge_sort(lista[mijloc:])

    return interclaseaza(stanga, dreapta)

def interclaseaza(stanga, dreapta):
    rezultat = []
    i = 0
    j = 0

    while i < len(stanga) and j < len(dreapta):
        if stanga[i] < dreapta[j]:
            rezultat.append(stanga[i])
            i += 1
        else:
            rezultat.append(dreapta[j])
            j += 1

    rezultat.extend(stanga[i:])
    rezultat.extend(dreapta[j:])

    return rezultat

print("Introdu numerele pe care vrei sa le sortezi, separate prin spatiu:")
date_intrare = input()

numere = [int(x) for x in date_intrare.split()]

print("\nLista initiala:", numere)

lista_sortata = merge_sort(numere)

print("Lista sortata:", lista_sortata)