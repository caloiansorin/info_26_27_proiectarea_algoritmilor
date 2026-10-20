n = int(input("Introdu dimensiunea vectorului: "))
v = []
for i in range(n):
    numar = int(input(f"citim numarul de pe indexul {i}: "))
    v.append(numar)

for i in range(1, n):
    key = v[i]
    j = i - 1
    while j >= 0 and v[j] > key:
        v[j + 1] = v[j]
        j -= 1
    v[j + 1] = key
print("Vectorul sortat:", v)