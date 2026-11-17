def pancake_sort(v):
    for i in range(len(v), 1, -1):
        m = max(v[:i]) # nr maxim 
        idx = v.index(m) # index ul lui m 
        if idx > 0:
            v[:idx + 1] = v[:idx + 1][::-1] # rasturnare aduce la index 0
        v[:i] = v[:i][::-1]  # rasturnare duce la sfarsitul vectorul 
    return v

x = [3, 2, 4, 1, 5, 10, 69, 67, 51]
pancake_sort(x)
print(x)