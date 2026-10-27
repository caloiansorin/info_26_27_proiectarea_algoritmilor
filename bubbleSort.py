n = int(input("Introdu dimensiunea vectorului: "))
v = []

for i in range(n):
    numar = int(input(f"citim numarul de pe indexul {i}: "))
    v.append(numar)

# bubble sort
for i in range(n - 1):
    for j in range(i + 1, n):
        if v[i] > v[j]:
            v[i], v[j] = v[j], v[i]

print("Vectorul sortat:", v)