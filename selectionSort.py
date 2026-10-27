n = int(input("Introduceti numarul de elemente: "))
v = []

for i in range(n):
    numar = int(input(f"Elementul de pe pozitia {i}: "))
    v.append(numar)

print("Vectorul initial este:", v)

for i in range(n - 1):
    # Presupunem ca elementul curent este cel mai mic
    poz_min = i
    # Cautam daca exista un element si mai mic in restul vectorului
    for j in range(i + 1, n):
        if v[j] < v[poz_min]:
            poz_min = j  # retinem noua pozitie a minimului
            
    # Interschimbam elementul de pe pozitia i cu cel minim gasit
    v[i], v[poz_min] = v[poz_min], v[i]

# 4. Afisarea rezultatului final
print("Vectorul sortat crescator este:", v)