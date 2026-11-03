def counting_sort(vector):
    if not vector:
        return vector
    
    val_max = max(vector)
    
    count = [0] * (val_max + 1)
    for numar in vector :
        count[numar] += 1
    
    index = 0
    for val in range(len(count)):
        for i in range(count[val]):
            vector[index] = val
            index +=1
            
    return vector


v = [4,2,3,1,1,3,2,4,6,43,23,12]
print("Initial", v)

counting_sort(v)
print("Sortat : ", v)