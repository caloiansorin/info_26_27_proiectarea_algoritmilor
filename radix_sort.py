def radix_sort_pozitive(lista):
    if not lista:
        return []

    rezultat = lista.copy()
    maxim = max(rezultat)
    exponent = 1

    while maxim // exponent > 0:
        galeti = [[] for _ in range(10)]

        for numar in rezultat:
            cifra = (numar // exponent) % 10
            galeti[cifra].append(numar)

        rezultat = []

        for galet in galeti:
            rezultat.extend(galet)

        exponent *= 10

    return rezultat


def radix_sort(lista):
    negative = [-x for x in lista if x < 0]
    pozitive = [x for x in lista if x >= 0]

    negative = radix_sort_pozitive(negative)
    pozitive = radix_sort_pozitive(pozitive)

    negative = [-x for x in reversed(negative)]

    return negative + pozitive


numere = [170, 45, 75, -90, 802, 24, 2, 66, -15, 0]

print("Lista initiala:", numere)
print("Lista sortata:", radix_sort(numere))