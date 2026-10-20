def merge(left, right):
    resultat = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            resultat.append(left[i])
            i += 1
        else:
            resultat.append(right[j])
            j += 1
            
    resultat.extend(left[i:])
    resultat.extend(right[j:])
    
    return resultat

def mergeSort(arr):
    step = 1
    length = len(arr)
    
    while step < length:
        for i in range(0, length, 2 * step):
            left = arr[i:i + step]
            right = arr[i + step:i + 2 * step]
            
            merged = merge(left, right)
            
            for j, val in enumerate(merged):
                arr[i + j] = val
                
        step *= 2
        
    return arr

sirNesortat = [23, 7, 56, 10, 15, 23, 45, 13]
sirSortat = mergeSort(sirNesortat)
print("Sirul este sortat:", sirSortat)