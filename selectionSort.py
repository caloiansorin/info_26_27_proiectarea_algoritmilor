n = int(input("citim numarul de elemente: "))
v = []
for i in range(n):
    numar = int(input(f"citim numarul de pe indexul {i}: "))
    v.append(numar)
#selection sort
for i in range(n):
    min_index = i
    for j in range(i + 1, n):
        if v[j] < v[min_index]:
            min_index = j
    v[i], v[min_index] = v[min_index], v[i]
print("Vectorul sortat:", v)