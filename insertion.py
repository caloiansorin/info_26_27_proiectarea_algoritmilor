# proiectarea algortmilor

# insertion sort

numere = [8, 3, 6, 2, 7, 1, 5]
print(numere)
for pozitie_curenta in range(1, len(numere)):
    numar_de_inserat = numere[pozitie_curenta]
    pozitie_comparata = pozitie_curenta - 1

    while (pozitie_comparata >= 0
           and numere[pozitie_comparata] > numar_de_inserat):
        # copiem numarul mai mare cu o pozitie la dreapta
        numere[pozitie_comparata + 1] = numere[pozitie_comparata]
        pozitie_comparata -= 1
        # print(numere) (ca sa observam ce mai exact se intampla in lista)

    # asezam numarul in locul ramas liber
    
    numere[pozitie_comparata + 1] = numar_de_inserat

print(numere)
