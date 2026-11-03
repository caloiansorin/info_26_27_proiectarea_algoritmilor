def counting_sort(arr):
    if not arr:
        return arr

    max_val = max(arr)
    count = [0] * (max_val + 1)
    output = [0] * len(arr)

    for num in arr:
        count[num] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for i in range(len(arr) - 1, -1, -1):
        num = arr[i]
        output[count[num] - 1] = num
        count[num] -= 1

    return output

if __name__ == "__main__":
    date = input("Introduceți numere întregi pozitive, separate prin spațiu: ")
    lista = [int(x) for x in date.split()]
    
    print("Lista sortată este:", counting_sort(lista))