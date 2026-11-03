def counting_sort(a):
    if not a:
        return []

    max_val = max(a)

    # Pasul 1: numărăm aparițiile
    cnt = [0] * (max_val + 1)
    for x in a:
        cnt[x] += 1

    # Pasul 2: sume parțiale
    for i in range(1, max_val + 1):
        cnt[i] += cnt[i - 1]

    # Pasul 3: construim rezultatul (de la dreapta la stânga)
    out = [0] * len(a)
    for i in range(len(a) - 1, -1, -1):
        x = a[i]
        out[cnt[x] - 1] = x
        cnt[x] -= 1

    return out


if __name__ == "__main__":
    a = [4, 2, 2, 8, 3, 3, 1]
    print(counting_sort(a))   # [1, 2, 2, 3, 3, 4, 8]