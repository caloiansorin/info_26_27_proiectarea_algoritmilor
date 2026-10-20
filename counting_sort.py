def counting_sort(lista):
    if not lista:
        return []

    minim = min(lista)
    maxim = max(lista)

    frecvente = [0] * (maxim - minim + 1)

    for numar in lista:
        frecvente[numar - minim] += 1

    rezultat = []

    for i, frecventa in enumerate(frecvente):
        rezultat.extend([i + minim] * frecventa)

    return rezultat


numere = [4, 2, -3, 6, 2, 0, -1, 4, 1]

print("Lista initiala:", numere)
print("Lista sortata:", counting_sort(numere))