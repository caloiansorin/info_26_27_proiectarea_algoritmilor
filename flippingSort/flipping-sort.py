def flip(arr, k):
    arr[:k+1] = reversed(arr[:k+1])

def pancake_sort(arr):
    n = len(arr)
    
    for unsorted_bit in range(n, 1, -1):
        max_idx = arr.index(max(arr[:unsorted_bit]))
        
        if max_idx != unsorted_bit - 1:
            if max_idx != 0:
                flip(arr, max_idx)
                
            flip(arr, unsorted_bit - 1)
            
    return arr

date_intrare = input("Introdu numerele separate prin spatiu: ")
clatite = [int(x) for x in date_intrare.split()]

print("Lista initiala:", clatite)
pancake_sort(clatite)
print("Lista sortata:", clatite)