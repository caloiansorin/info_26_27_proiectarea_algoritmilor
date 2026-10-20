v = [5, 2, 4, 1]

n = len(v)

for i in range(n - 1):
    for j in range(n - 1 - i):
        if v[j] > v[j + 1]:
            aux = v[j]
            v[j] = v[j + 1]
            v[j + 1] = aux

print(v)