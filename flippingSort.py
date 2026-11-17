def gaseste_maxim(v, size):
    pozitie_maxim = 0
    valoare_maxima = v[0]
    
    # Un for simplu și curat de la 1 până la size - 1
    for i in range(1, size):
        if v[i] > valoare_maxima:
            valoare_maxima = v[i]
            pozitie_maxim = i
            
    return pozitie_maxim

def inverseaza_portiune(v, capat):
    for i in range((capat + 1) // 2):
        aux = v[i]
        v[i] = v[capat - i]
        v[capat - i] = aux

def flipping_sort(v):
    lista_lucru = []
    for element in v:
        lista_lucru.append(element)
        
    n = len(lista_lucru)
    size = n
    
    while size > 1:
        # 1. Găsim poziția maximului
        pozitie_maxim = gaseste_maxim(lista_lucru, size)
        
        # 2. Dacă maximul nu e la sfârșit, îl mutăm
        if pozitie_maxim != size - 1:
            
            # Dacă nu e pe prima poziție, îl ducem primul
            if pozitie_maxim != 0:
                inverseaza_portiune(lista_lucru, pozitie_maxim)
                
            # Trimitem maximul la sfârșitul porțiunii nesortate
            inverseaza_portiune(lista_lucru, size - 1)
            
        size = size - 1
        
    return lista_lucru

n = int(input("Introduceti numarul de elemente: "))

vector = []
for i in range(n):
    elem = int(input(f"Elementul {i + 1}: "))
    vector.append(elem)

print("\nVectorul introdus este:")
print(vector)

vector_sortat = flipping_sort(vector)

print("\nVectorul sortat crescator este:")
print(vector_sortat)