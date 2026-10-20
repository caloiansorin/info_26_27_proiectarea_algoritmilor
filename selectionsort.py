
v = [7, 4, 6, 2, 5]

n = len(v)

for i in range(n - 1):
    poz_min = i

    for j in range(i + 1, n):
        if v[j] < v[poz_min]:
            poz_min = j

    aux = v[i]
    v[i] = v[poz_min]
    v[poz_min] = aux

print(v)
