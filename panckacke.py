def flip(arr, k):
    """Переворачивает первые k элементов (лопатка под k-м блином)."""
    arr[:k] = arr[:k][::-1]


def pancake_sort(arr):
    n = len(arr)


    for size in range(n, 1, -1):


        max_index = arr.index(max(arr[:size]))

        
        if max_index == size - 1:
            continue

       
        if max_index != 0:
            flip(arr, max_index + 1)
            print(f"Переворот {max_index + 1}: {arr}  ← максимум {arr[0]} наверху")

       
        flip(arr, size)
        print(f"Переворот {size}: {arr}  ← {arr[size - 1]} на месте")

    return arr


# Пример
blini = [3, 6, 1, 5, 2, 4]
print("Начало:      ", blini)
pancake_sort(blini)
print("Результат:   ", blini)