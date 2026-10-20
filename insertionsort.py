
v = [6, 3, 5, 2]
n = len(v)

for i in range(1, n):
    aux = v[i]
    j = i - 1

    while j >= 0 and v[j] > aux:
        v[j + 1] = v[j]
        j = j - 1

    v[j + 1] = aux

print(v)
