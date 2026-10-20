n=int(input("Introdu dimensiunea vectorului: "))
v=[]
for i in range(n):
    numar=int(input(f"citim numarul de pe indexul {i}: "))
    v.append(numar)
#merge sort
def merge_sort(v):
    if len(v) > 1:
        mid = len(v) // 2
        left_half = v[:mid]
        right_half = v[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                v[k] = left_half[i]
                i += 1
            else:
                v[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            v[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            v[k] = right_half[j]
            j += 1
            k += 1
    
#afiseaza vectorul sortat
print("Vectorul sortat:", v)