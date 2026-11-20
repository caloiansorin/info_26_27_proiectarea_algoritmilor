def flip(lista, k):
    left = 0
    right = k - 1
    
    while left < right:
        aux = lista[left]
        lista[left] = lista[right]
        lista[right] = aux
        left += 1
        right -= 1 

    
    
def flippingSort(lista):
    numberEle = len(lista)
    
    for i in range(numberEle,1,-1):
        maxIndex = 0
        for j in range(1,i):
            if lista[j] > lista[maxIndex]:
                maxIndex = j
        flip(lista, maxIndex+1)
        flip(lista, i)
    return lista
    
    
    
lista = [3, 6, 1, 5, 2, 4]
flippingSort(lista)
print(lista)
