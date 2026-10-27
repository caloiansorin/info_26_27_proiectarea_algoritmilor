def quicksort(arr):
    if len(arr) <= 1:
        return arr
        
    pivot = arr[-1]
    stanga = [x for x in arr[:-1] if x <= pivot]
    dreapta = [x for x in arr[:-1] if x > pivot]
    
    return quicksort(stanga) + [pivot] + quicksort(dreapta)

if __name__ == "__main__":
    date = input("Introduceți numerele separate prin spațiu: ")
    lista = [int(x) for x in date.split()]
    print("Lista sortată este:", quicksort(lista))