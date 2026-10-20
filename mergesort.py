
def merge_sort(v):
    if len(v) <= 1:
        return v

    mijloc = len(v) // 2

    stanga = merge_sort(v[:mijloc])
    dreapta = merge_sort(v[mijloc:])

    rezultat = []
    i = 0
    j = 0

    while i < len(stanga) and j < len(dreapta):
        if stanga[i] < dreapta[j]:
            rezultat.append(stanga[i])
            i = i + 1
        else:
            rezultat.append(dreapta[j])
            j = j + 1

    while i < len(stanga):
        rezultat.append(stanga[i])
        i = i + 1

    while j < len(dreapta):
        rezultat.append(dreapta[j])
        j = j + 1

    return rezultat


v = [8, 3, 6, 2]

v = merge_sort(v)

print(v)
