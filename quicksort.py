def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i+1], array[high] = array[high], array[i+1]
    return i+1

def quicksort(arr, mic=0, mare=None):
    if mare is None:
        mare = len(arr) - 1

    if mic < mare:
        pivot = partition(arr, mic, mare)
        quicksort(arr, mic, pivot-1)
        quicksort(arr, pivot+1, mare)

sir = [64, 34, 25, 12, 22, 11, 90, 5]
quicksort(sir)
print("Sorted array:", sir)

#Python