def counting_sort(v):
    maxim = max(v)

    frecventa = [0] * (maxim + 1)

    for x in v:
        frecventa[x] += 1

    rezultat = []

    for i in range(len(frecventa)):
        for j in range(frecventa[i]):
            rezultat.append(i)

    return rezultat

n = int(input("Cate numere introduci? "))

v = []

for i in range(n):
    x = int(input("Introdu un numar: "))
    v.append(x)

print("Vectorul initial:", v)

v = counting_sort(v)

print("Vectorul sortat:", v)