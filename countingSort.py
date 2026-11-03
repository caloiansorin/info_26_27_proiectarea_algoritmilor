def counting_sort(numbers):
	# Pentru o listă goală, sortarea este deja finalizată.
	if len(numbers) == 0:
		return numbers
	# Determinăm intervalul de valori care trebuie numărate.
	biggest = max(numbers)
	smallest = min(numbers)
	count = [0] * (biggest - smallest + 1)

	# Numărăm aparițiile fiecărui element folosind un index ajustat.
	for number in numbers:
		count[number - smallest] += 1

	# Reconstruim lista în ordine crescătoare pe baza frecvențelor.
	result = []
	for i in range(len(count)):
		for j in range(count[i]):
			result.append(i + smallest)

	return result


numbers = [4, 2, 2, 8, 3, 3, 1]
print(counting_sort(numbers))
