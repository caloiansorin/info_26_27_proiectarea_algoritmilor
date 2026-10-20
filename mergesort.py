def merge_sort(v):
    if len(v) <= 1:
        return v
    mijloc = len(v) // 2
    stanga = merge_sort(v[:mijloc])
    dreapta = merge_sort(v[mijloc:])
    return merge(stanga, dreapta)

def merge(stanga, dreapta):
    rezultat = []
    i = 0
    j = 0
    
    while i < len(stanga) and j < len(dreapta):
        if stanga[i] <= dreapta[j]:
            rezultat.append(stanga[i])
            i += 1
        else:
            rezultat.append(dreapta[j])
            j += 1
            
    while i < len(stanga):
        rezultat.append(stanga[i])
        i += 1
        
    while j < len(dreapta):
        rezultat.append(dreapta[j])
        j += 1
        
    return rezultat

vector = [38, 27, 43, 3, 9, 82, 10]
print(merge_sort(vector))