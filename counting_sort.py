

def counting_sort(a):
    if not a:
        return []

    mn, mx = min(a), max(a)
    f = [0] * (mx - mn + 1)

    # parcurgerea 1: numărare
    for x in a:
        f[x - mn] += 1

    # parcurgerea 2: rescriere în ordine
    i = 0
    for v in range(len(f)):
        while f[v] > 0:
            a[i] = v + mn
            i += 1
            f[v] -= 1

    return a


if __name__ == "__main__":
    v = [5, 2, 9, 1, 5, 6, -3, 0, 2]
    print("Vector initial:", v)
    print("Vector sortat: ", counting_sort(v[:]))
