numbers = [0, 1, 2, 3, 3, 2, 1, 0, 4, 5]

counts = [0] * (max(numbers) + 1)

for number in numbers:
    counts[number] += 1

positions = counts.copy()

for index in range(1, len(positions)):
    positions[index] += positions[index - 1]

sorted_numbers = [0] * len(numbers)

for number in reversed(numbers):
    target_index = positions[number] - 1
    sorted_numbers[target_index] = number
    positions[number] -= 1

print(sorted_numbers)