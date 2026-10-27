lista=[1, 8, 3, 6, 9, 5, 7, 4]

def mergesort(lista):
    if len(lista)<=1:
        return lista

    mij=len(lista)//2
    st=lista[:mij]
    dr=lista[mij:]
    sortatst=mergesort(st)
    sortatdr=mergesort(dr)
    return merge(sortatst, sortatdr)

def merge(st,dr):
    rezultat=[]
    i=j=0
    while i<len(st) and j<len(dr):
        if st[i]<dr[j]:
            rezultat.append(st[i])
            i=i+1
        else:
            rezultat.append(dr[j])
            j=j+1
    rezultat.extend(st[i:])
    rezultat.extend(dr[j:])
    return rezultat

print (mergesort(lista))
