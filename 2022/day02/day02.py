SCORES = {
	'A X': 4,
	'A Y': 8,
	'A Z': 3,
	'B X': 1,
	'B Y': 5,
	'B Z': 9,
	'C X': 7,
	'C Y': 2,
	'C Z': 6,
}

CHOICES = {
	'A X': 'Z',
	'A Y': 'X',
	'A Z': 'Y',
	'B X': 'X',
	'B Y': 'Y',
	'B Z': 'Z',
	'C X': 'Y',
	'C Y': 'Z',
	'C Z': 'X',
}

with open('input.txt', 'r') as f:
	lines = f.read().splitlines()
print(f'Part 1: {sum([SCORES[line] for line in lines])}')
lines = [line[:-1] + CHOICES[line] for line in lines]
print(f'Part 2: {sum([SCORES[line] for line in lines])}')
