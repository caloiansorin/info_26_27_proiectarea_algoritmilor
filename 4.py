# Selection Sort – sortare prin selecție
# Complexitate: O(n^2) în toate cazurile; in-place, puține interschimbări

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        # Căutăm indicele celui mai mic element din partea nesortată
        idx_min = i
        for j in range(i + 1, n):
            if arr[j] < arr[idx_min]:
                idx_min = j

        # Îl aducem pe poziția i
        if idx_min != i:
            arr[i], arr[idx_min] = arr[idx_min], arr[i]
    return arr


if __name__ == "__main__":
    date = [64, 25, 12, 22, 11]
    print("Inițial:", date)
    print("Sortat: ", selection_sort(date.copy()))