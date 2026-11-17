# Quick Sort – sortare rapidă prin partiționare
# Complexitate: O(n log n) în medie, O(n^2) în cel mai rău caz; sortare in-place

def quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low < high:
        # Partiționăm și obținem poziția finală a pivotului
        p = partitionare(arr, low, high)
        # Sortăm recursiv partea stângă și partea dreaptă
        quick_sort(arr, low, p - 1)
        quick_sort(arr, p + 1, high)
    return arr


def partitionare(arr, low, high):
    # Alegem ultimul element ca pivot (schema Lomuto)
    pivot = arr[high]
    i = low - 1  # granița elementelor mai mici decât pivotul

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Punem pivotul pe poziția sa corectă
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


if __name__ == "__main__":
    date = [10, 7, 8, 9, 1, 5]
    print("Inițial:", date)
    print("Sortat: ", quick_sort(date.copy()))