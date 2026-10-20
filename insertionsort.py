lista=[1, 8, 3, 6, 9, 5, 7, 4]
n=len(lista)
for i in range(1, n):
    insert_index=i
    current_value=lista[i]
    for j in range (i-1, -1, -1):
        if lista[j]>current_value:
            lista[j+1]=lista[j]
            insert_index=j
        else:
            break
        lista[insert_index]=current_value
print(lista) 