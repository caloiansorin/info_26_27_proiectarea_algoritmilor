def rastoarna_lista(lista, punct_de_oprire):
    punct_de_pornire = 0
    while punct_de_pornire < punct_de_oprire:
        lista[punct_de_pornire], lista[punct_de_oprire] = lista[punct_de_oprire], lista[punct_de_pornire]
        punct_de_pornire += 1
        punct_de_oprire -= 1

def gaseste_pozitia_maximului(lista, lungime_zona_cautare):
    pozitie_maxim = 0
    for pozitie_curenta in range(1, lungime_zona_cautare):
        if lista[pozitie_curenta] > lista[pozitie_maxim]:
            pozitie_maxim = pozitie_curenta
    return pozitie_maxim

def sortare_prin_rasturnare(lista):
    total_elemente = len(lista)
    for dimensiune_zona_nesortata in range(total_elemente, 1, -1):
        pozitie_maxim = gaseste_pozitia_maximului(lista, dimensiune_zona_nesortata)
        if pozitie_maxim != dimensiune_zona_nesortata - 1:
            if pozitie_maxim != 0:
                rastoarna_lista(lista, pozitie_maxim)
            rastoarna_lista(lista, dimensiune_zona_nesortata - 1)
    return lista


text_introdus = input("Introdu numerele separate prin spațiu: ")

numere_de_sortat = [int(numar) for numar in text_introdus.split()]

sortare_prin_rasturnare(numere_de_sortat)

print("Lista sortată este:", numere_de_sortat)