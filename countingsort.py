def countingSort(arr):
    if not arr:
        return arr
        
    max_val = max(arr)
    count = [0] * (max_val + 1)

    for num in arr:
        count[num] += 1
        
    arr[:] = []

    for num, freq in enumerate(count):
        arr.extend([num] * freq)

    return arr

sirNesortat = [4, 2, 2, 6, 3, 3, 1, 6, 5, 2, 3]
sirSortat = countingSort(sirNesortat)
print("Sorted array:", sirSortat)