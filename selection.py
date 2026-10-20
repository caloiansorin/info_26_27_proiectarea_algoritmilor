# selection sort

def swap_list(lista, a, b):
    lista[a], lista[b] = lista[b], lista[a]

Lista = [8, 2, 5, 4, 3, 1, 6]

for i in range(len(Lista)): # 1. parcurgem lista
    min_index = i # asumam ca numaru curent e cel mai mic
    for j in range(i + 1, len(Lista)):
        if Lista[j] < Lista[min_index]: # gasim cel mai mic numar din partea nesortata a listei
            min_index = j
    swap_list(Lista, i, min_index) # interschimbam numarul pe care l-am presupus cu cel mai mic
    print(Lista)

print(Lista)
