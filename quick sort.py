
def quick_sort(lista):
    
    if len(lista) <= 1:
        return lista

    pivot = lista[-1]

    rest = lista[:-1]

    stanga = []
    dreapta = []

    for x in rest:
        if x <= pivot:
            stanga.append(x)
        else:
            dreapta.append(x)

    return quick_sort(stanga) + [pivot] + quick_sort(dreapta)


n = int(input("Introdu numarul de elemente: "))

numere = []

for i in range(n):
    x = int(input("Introdu un numar: "))
    numere.append(x)

rezultat = quick_sort(numere)
print("Lista sortata:", rezultat)
