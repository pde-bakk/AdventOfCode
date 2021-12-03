def find_most_common_value(r: list, idx: int) -> str:
	zeroes, ones = 0, 0
	for row in r:
		if row[idx] == '0':
			zeroes += 1
		elif row[idx] == '1':
			ones += 1
	if zeroes > ones:
		return '0'
	return '1'


def part1():
	gamma, epsilon = '', ''
	for i in range(len(rows[0])):
		most_common = find_most_common_value(rows, i)
		gamma += most_common
		epsilon += str(int(not int(most_common)))
	print(f'Gamma: {gamma} ({int(gamma, 2)}), Epsilon: {epsilon} ({int(epsilon, 2)})')

	return int(gamma, 2) * int(epsilon, 2)


def get_rating(r: list, co2: bool):
	length = len(r[0])
	for i in range(length):
		if len(r) == 1:
			break
		currbit = find_most_common_value(r, i)
		if co2:
			currbit = str(int(not int(currbit)))
		r = [row for row in r if row[i] == currbit]
	return r[0]


def part2(r: list):
	oxygen = get_rating(r, False)
	co2 = get_rating(r, True)
	print(oxygen, co2)
	print(f'oxygen: {oxygen} ({int(oxygen, 2)}), co2: {co2} ({int(co2, 2)})')
	return int(oxygen, 2) * int(co2, 2)


rows = open('input.txt').read().splitlines()
# print(f'part1: {part1()}')
print(f'part2: {part2(rows)}')
