def bubble_sort(v):
    n  = len(v)
    for i in range(n-1):
        for j in range (i+1,n):
            if v[j] < v[i]:
                v[j],v[i] = v[i],v[j]
                
    return v

vector = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(vector))