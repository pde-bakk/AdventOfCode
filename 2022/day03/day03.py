with open('input.txt', 'r') as f:
	lines = f.read().splitlines()

total = 0
for i, line in enumerate(lines):
	first, second = line[:len(line)//2], line[len(line)//2:]
	common = set(first) & set(second)
	for item in common:
		if item.islower():
			value = ord(item) - ord('a') + 1
		else:
			value = ord(item) - ord('A') + 27
		total += value
print(f'Part 1: {total}')

elfs = []
total = 0
for i, line in enumerate(lines):
	if i % 3 == 0:
		elfs.clear()
	elfs.append(set(line))

	if i % 3 == 2:
		common = elfs[0] & elfs[1] & elfs[2]
		for item in common:
			if item.islower():
				value = ord(item) - ord('a') + 1
			else:
				value = ord(item) - ord('A') + 27
			total += value
print(f'Part 2: {total}')
