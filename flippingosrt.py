def flippingsort(lista):
    for i in range(len(lista)):
        poz=lista.index(max(lista[:len(lista)-i]))
        if poz==0:
            lista[:len(lista)-i]=lista[:len(lista)-i][::-1]
        else:
            lista[:len(lista)-i]=lista[:poz+1][::-1]+lista[poz+1:len(lista)-i]
        lista[:len(lista)-i]=lista[:len(lista)-i][::-1]
    return lista

lista=[9, 2, 4, 5, 6, 3, 8, 1]
listasortata = flippingsort(lista)
print(listasortata)