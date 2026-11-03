def countingsort(lista):
  count1 = max(lista)
  count2 = [0] * (count1 + 1)

  while len(lista) > 0:
    num = lista.pop(0)
    count2[num] += 1

  for i in range(len(count2)):
    while count2[i] > 0:
      lista.append(i)
      count2[i] -= 1

  return lista

list = [4, 2, 2, 6, 3, 3, 1, 6, 5, 2, 3]
listasortata = countingsort(list)
print(listasortata)