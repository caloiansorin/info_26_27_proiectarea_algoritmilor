n = int(input("Introdu dimensiunea vectorului: "))
v = []

for i in range(n):
    numar = int(input(f"Elementul de pe pozitia {i}: "))
    v.append(numar)

print("Vectorul initial este:", v)

# Pornim de la al doilea element (index 1), pentru ca primul e deja "sortat"
for i in range(1, n):
    # Luam elementul curent pe care vrem sa il asezam la locul lui
    element_curent = v[i]
    # Pornim comparatia cu vecinul din stanga sa
    j = i - 1
    # Cat timp mai avem elemente in stanga (j >= 0)
    # si gasim numere mai mari decat elementul nostru curent:
    while j >= 0 and v[j] > element_curent:
        v[j + 1] = v[j]
        j = j - 1
    # Am gasit locul liber potrivit si inseram elementul curent
    v[j + 1] = element_curent
print("Vectorul sortat este:", v)