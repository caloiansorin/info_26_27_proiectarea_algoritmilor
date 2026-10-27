def quick_sort(lista):    
    if len(lista) <= 1:           #verificam daca lista are 1 element sau mai putin, caz in care deja sortata
        return lista

    pivot = lista[len(lista) // 2]    #selectam pivotul

    mici = [x for x in lista if x < pivot]   #facem 3 liste, una pentru nr mai mici decat pivot
    egale = [x for x in lista if x == pivot]               # una pentru cele egale
    mari = [x for x in lista if x > pivot]                 # una pentru cele mari

    return quick_sort(mici) + egale + quick_sort(mari)     #folosind reursivitatea, le sortam si concatenam


numere = [7, 2, 9, 4, 1, 8, 4]
print(quick_sort(numere))  # [1, 2, 4, 4, 7, 8, 9]         