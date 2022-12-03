with open('input.txt', 'r') as f:
	lines = f.read().splitlines()

total = 0
for line in lines:
	first, second = line[:len(line)//2], line[len(line)//2:]
	common = set(first) & set(second)
	for item in common:
		if item.islower():
			value = ord(item) - ord('a') + 1
		else:
			value = ord(item) - ord('A') + 27
		print(value)
		total += value
print(total)
