def counting_sort_by_digit(v, exp):
    n = len(v)
    output = [0] * n
    count = [0] * 10

    # 1) Numără apariția fiecărei cifre (0-9)
    for x in v:
        digit = (x // exp) % 10
        count[digit] += 1

    # 2) Transformă count în sume parțiale (poziții finale)
    for i in range(1, 10):
        count[i] += count[i - 1]

    # 3) Construiește output parcurgând de la sfârșit (pentru stabilitate)
    for i in range(n - 1, -1, -1):
        digit = (v[i] // exp) % 10
        output[count[digit] - 1] = v[i]
        count[digit] -= 1

    return output


def radix_sort(v):
    if not v:
        return v

    max_val = max(v)
    exp = 1

    while max_val // exp > 0:
        v = counting_sort_by_digit(v, exp)
        exp *= 10

    return v


if __name__ == "__main__":
    v = [170, 45, 75, 90, 802, 24, 2, 66]
    print(radix_sort(v))   # [2, 24, 45, 66, 75, 90, 170, 802]