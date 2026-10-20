def merge_sort(lista):
    # O lista cu 0 sau 1 element este deja sortata.
    if len(lista) <= 1:
        return lista

    mijloc = len(lista) // 2
    prima_jumatate = merge_sort(lista[:mijloc])
    a_doua_jumatate = merge_sort(lista[mijloc:])

    lista_sortata = []
    index_prima = 0
    index_a_doua = 0

    # Comparam elementele de la inceputul fiecarei jumatati.
    while index_prima < len(prima_jumatate) and index_a_doua < len(a_doua_jumatate):
        if prima_jumatate[index_prima] <= a_doua_jumatate[index_a_doua]:
            lista_sortata.append(prima_jumatate[index_prima])
            index_prima += 1
        else:
            lista_sortata.append(a_doua_jumatate[index_a_doua])
            index_a_doua += 1

    # Adaugam elementele ramase (daca mai exista) in lista sortata.
    lista_sortata.extend(prima_jumatate[index_prima:])
    lista_sortata.extend(a_doua_jumatate[index_a_doua:])
    return lista_sortata


numere = [8, 3, 6, 2, 7, 1, 5]
print("Lista initiala:", numere)
numere_sortate = merge_sort(numere)
print("Lista sortata:", numere_sortate)