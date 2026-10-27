def Partitioneaza(A, st, dr) :
    pivot = A[dr]
    i = st - 1
    
    for j in range(st, dr) :
        if A[j] <= pivot :
            i = i + 1
            A[i], A[j] = A[j], A[i]
             
    A[i + 1], A[dr] = A[dr], A[i + 1]
    return i + 1

def Quick_Sort(A, st, dr) :
    if st < dr :
        q = Partitioneaza(A, st, dr)
        Quick_Sort(A, st, q - 1)
        Quick_Sort(A, q + 1, dr)
        
        
vector = [1, 9, 0 , 3, 12, 4]
Quick_Sort(vector,0,len(vector) - 1)
print(vector)