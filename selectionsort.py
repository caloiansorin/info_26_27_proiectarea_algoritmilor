lista=[1, 8, 3, 6, 9, 5, 7, 4]
n=len(lista)
for i in range (n-1):
    min_index=i
    for j in range(i+1, n):
        if lista[j]<lista[min_index]:
            min=j
    min_value=lista.pop(min_index)
    lista.insert(i, min_value)
print(lista)