# Merge Sort – sortare prin interclasare
# Complexitate: O(n log n) în toate cazurile; memorie suplimentară O(n)

def merge_sort(arr):
    # Cazul de bază: un element (sau niciunul) este deja sortat
    if len(arr) <= 1:
        return arr

    # Împărțim lista în două jumătăți
    mijloc = len(arr) // 2
    stanga = merge_sort(arr[:mijloc])
    dreapta = merge_sort(arr[mijloc:])

    # Interclasăm cele două jumătăți sortate
    return interclasare(stanga, dreapta)


def interclasare(stanga, dreapta):
    rezultat = []
    i = j = 0

    # Comparăm elementele și le adăugăm în ordine
    while i < len(stanga) and j < len(dreapta):
        if stanga[i] <= dreapta[j]:
            rezultat.append(stanga[i])
            i += 1
        else:
            rezultat.append(dreapta[j])
            j += 1

    # Adăugăm elementele rămase (una din liste va fi deja goală)
    rezultat.extend(stanga[i:])
    rezultat.extend(dreapta[j:])
    return rezultat


if __name__ == "__main__":
    date = [38, 27, 43, 3, 9, 82, 10]
    print("Inițial:", date)
    print("Sortat: ", merge_sort(date))