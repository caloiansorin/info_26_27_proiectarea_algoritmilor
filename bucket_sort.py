def bucket_sort(lista):
    if len(lista) <= 1:
        return lista.copy()

    minim = min(lista)
    maxim = max(lista)

    if minim == maxim:
        return lista.copy()

    numar_galeti = len(lista)
    galeti = [[] for _ in range(numar_galeti)]

    for numar in lista:
        index = int(
            (numar - minim) / (maxim - minim) * (numar_galeti - 1)
        )
        galeti[index].append(numar)

    rezultat = []

    for galet in galeti:
        galet.sort()
        rezultat.extend(galet)

    return rezultat


numere = [42, 32, 33, 52, 37, 47, 51, 20]

print("Lista initiala:", numere)
print("Lista sortata:", bucket_sort(numere))