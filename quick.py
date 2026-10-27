# alegi pivot, bagi numere mari la dreapta numere mici la stanga in aceeasi ordine
# cum apar ele in lista
# repeti cu sublistele create pana sunt ordonate

def quick_sort(lista):
    if len(lista) <= 1:
        return lista

    pivot = lista[0]
    mai_mici = []
    egale = [pivot]
    mai_mari = []

    for numar in lista[1:]:
        if numar < pivot:
            mai_mici.append(numar)
        elif numar == pivot:
            egale.append(numar)
        else:
            mai_mari.append(numar)

    return quick_sort(mai_mici) + egale + quick_sort(mai_mari)


print(quick_sort([9, 4, 9, 12]))

