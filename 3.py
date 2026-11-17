# Insertion Sort – sortare prin inserție
# Complexitate: O(n^2) în medie/rău, O(n) pe date deja sortate; in-place, stabil

def insertion_sort(arr):
    # Parcurgem de la al doilea element; partea din stânga e mereu sortată
    for i in range(1, len(arr)):
        cheie = arr[i]
        j = i - 1

        # Mutăm elementele mai mari decât cheia cu o poziție la dreapta
        while j >= 0 and arr[j] > cheie:
            arr[j + 1] = arr[j]
            j -= 1

        # Inserăm cheia pe locul eliberat
        arr[j + 1] = cheie
    return arr


if __name__ == "__main__":
    date = [12, 11, 13, 5, 6]
    print("Inițial:", date)
    print("Sortat: ", insertion_sort(date.copy()))