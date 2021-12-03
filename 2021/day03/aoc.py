def find_most_common_value(rows: list, idx: int) -> str:
	if len([1 for row in rows if row[idx] == '1']) >= len(rows) / 2:
		return '1'
	return '0'


def invert_value(bit: str) -> str:
	return str(int(not int(bit)))


def part1():
	gamma, epsilon = '', ''
	for i in range(len(lines[0])):
		most_common = find_most_common_value(lines, i)
		gamma += most_common
		epsilon += invert_value(most_common)
	print(f'Gamma: {gamma} ({int(gamma, 2)}), Epsilon: {epsilon} ({int(epsilon, 2)})')

	return int(gamma, 2) * int(epsilon, 2)


def get_rating(rows: list, co2: bool):
	length = len(rows[0])
	for i in range(length):
		if len(rows) == 1:
			break
		currbit = find_most_common_value(rows, i)
		if co2:
			currbit = invert_value(currbit)
		rows = [row for row in rows if row[i] == currbit]
	return rows[0]


def part2(r: list):
	oxygen = get_rating(r, False)
	co2 = get_rating(r, True)
	print(f'oxygen: {oxygen} ({int(oxygen, 2)}), co2: {co2} ({int(co2, 2)})')
	return int(oxygen, 2) * int(co2, 2)


lines = open('input.txt').read().splitlines()
print(f'part1: {part1()}')
print(f'part2: {part2(lines)}')
