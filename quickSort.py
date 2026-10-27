def quicksort(v):
    if len(v) <= 1:
        return v

    pivot = v[-1] # Alegem ultimul element ca pivot

    stanga = []
    dreapta = []

    # Parcurgem vectorul de la primul pana la penultimul element (fara pivot)
    for i in range(len(v) - 1):
        if v[i] <= pivot:
            stanga.append(v[i])  
        else:
            dreapta.append(v[i]) 
    return quicksort(stanga) + [pivot] + quicksort(dreapta)


n = int(input("Introduceti numarul de elemente: "))
vector = []
for i in range(n):
    elem = int(input(f"Elementul {i + 1}: "))
    vector.append(elem)

print("\nVectorul introdus este:")
print(vector)

vector_sortat = quicksort(vector)

print("Vectorul sortat crescator este:")
print(vector_sortat)