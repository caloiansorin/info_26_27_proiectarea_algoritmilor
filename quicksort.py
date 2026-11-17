def Rastoarna(A, st, dr) :
    while st < dr :
        A[st], A[dr] = A[dr], A[st]
        st = st + 1
        dr = dr - 1

def Gaseste_Maxim(A, st, dr) :
    max_idx = st
    for j in range(st + 1, dr + 1) :
        if A[j] > A[max_idx] :
            max_idx = j
    return max_idx

def Pancake_Sort(A, st, dr) :
    for i in range(dr, st, -1) :
        max_idx = Gaseste_Maxim(A, st, i)
        
        if max_idx != i :
            if max_idx != st :
                Rastoarna(A, st, max_idx)
            Rastoarna(A, st, i)
        
        
vector = [3, 2, 4, 1, 5]
Pancake_Sort(vector, 0, len(vector) - 1)
print(vector)