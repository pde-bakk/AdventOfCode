import re


lines = open('input.txt').readlines()
letters = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
part1 = 0
for line in lines:
	digits = [c for c in line if c.isdigit()]
	part1 += int(digits[0] + digits[-1])
print(part1)

part2 = 0
for line in lines:
	digits = [(i, c) for i, c in enumerate(line) if c.isdigit()]
	for value, letter in enumerate(letters, start=1):
		occs = [(m.start(), str(value)) for m in re.finditer(letter, line)]
		digits += occs
	first, last = min(digits), max(digits)
	part2 += int(first[1] + last[1])
print(part2)
