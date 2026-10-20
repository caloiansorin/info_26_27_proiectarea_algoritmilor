def selection_sort(lista):
    n = len(lista)
    
    for i in range(n):
        min_index = i
        
        for j in range(i + 1, n):
            if lista[j] < lista[min_index]:
                min_index = j
                
        lista[i], lista[min_index] = lista[min_index], lista[i]
        
    return lista

print("Introdu numerele pe care vrei sa le sortezi, separate prin spatiu:")
date_intrare = input()

numere = [int(x) for x in date_intrare.split()]

print("\nLista initiala:", numere)

lista_sortata = selection_sort(numere)

print("Lista sortata:", lista_sortata)