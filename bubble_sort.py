def bubble_sort(lista):
    n = len(lista)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                
    return lista

print("Introdu numerele pe care vrei sa le sortezi, separate prin spatiu:")
date_intrare = input()

numere = [int(x) for x in date_intrare.split()]

print("\nLista initiala:", numere)

lista_sortata = bubble_sort(numere)

print("Lista sortata:", lista_sortata)