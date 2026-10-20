class Nod:
    def __init__(self, valoare):
        self.valoare = valoare
        self.stanga = None
        self.dreapta = None


def insereaza(radacina, valoare):
    if radacina is None:
        return Nod(valoare)

    if valoare < radacina.valoare:
        radacina.stanga = insereaza(radacina.stanga, valoare)
    else:
        radacina.dreapta = insereaza(radacina.dreapta, valoare)

    return radacina


def parcurgere_inordine(radacina, rezultat):
    if radacina is not None:
        parcurgere_inordine(radacina.stanga, rezultat)
        rezultat.append(radacina.valoare)
        parcurgere_inordine(radacina.dreapta, rezultat)


def tree_sort(lista):
    radacina = None

    for numar in lista:
        radacina = insereaza(radacina, numar)

    rezultat = []
    parcurgere_inordine(radacina, rezultat)

    return rezultat


numere = [8, 3, 10, 1, 6, 14, 4, 7, 13, 3]

print("Lista initiala:", numere)
print("Lista sortata:", tree_sort(numere))