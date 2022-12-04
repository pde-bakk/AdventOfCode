with open('input.txt', 'r') as f:
	lines = f.read().splitlines()

part_1 = part_2 = 0
for line in lines:
	elfs = line.split(',')
	for i in range(2):
		A = [*map(int, elfs[i].split('-'))]
		A[-1] += 1
		elfs[i] = set(range(*A))
	if elfs[0] <= elfs[1] or elfs[1] <= elfs[0]:
		part_1 += 1
	if elfs[0] & elfs[1]:
		part_2 += 1
print(f'Part 1: {part_1}')
print(f'Part 2: {part_2}')
