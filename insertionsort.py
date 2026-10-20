def insertion_sort(v):
    for i in range(1, len(v)):
        cheie = v[i]
        j = i - 1
        while j >= 0 and v[j] > cheie:
            v[j + 1] = v[j]
            j -= 1
        v[j + 1] = cheie
    return v

vector = [12, 11, 13, 5, 6]
print(insertion_sort(vector))