def selection_sort(v):
    n = len(v)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if v[j] < v[min_idx]:
                min_idx = j
        v[i], v[min_idx] = v[min_idx], v[i]
    return v

vector = [64, 25, 12, 22, 11]
print(selection_sort(vector))