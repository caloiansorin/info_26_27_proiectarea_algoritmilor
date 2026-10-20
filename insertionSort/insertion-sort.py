def insertion_sort(lista):
    n = len(lista)
    
    for i in range(1, n):
        cheie = lista[i]
        j = i - 1
        
        while j >= 0 and cheie < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
            
        lista[j + 1] = cheie
        
    return lista

print("Introdu numerele pe care vrei sa le sortezi, separate prin spatiu:")
date_intrare = input()

numere = [int(x) for x in date_intrare.split()]

print("\nLista initiala:", numere)

lista_sortata = insertion_sort(numere)

print("Lista sortata:", lista_sortata)