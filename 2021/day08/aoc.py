def part1(rows: list[str]) -> int:
	total = 0
	for row in rows:
		_, output = row.split(' | ')
		output = output.split(' ')
		for item in output:
			total += int(len(set(item)) in (2, 3, 4, 7))
	return total


def set_easy(row: str) -> dict:
	patterns = {x: set() for x in range(10)}
	ops = row.replace(' | ', ' ').split(' ')
	for op in ops:
		opset = set(op)
		setlen = len(opset)
		if len(opset) in (2, 3, 4, 7):
			if setlen == 2:
				patterns[1] = opset
			elif setlen == 3:
				patterns[7] = opset
			elif setlen == 4:
				patterns[4] = opset
			else:
				patterns[8] = opset
		elif setlen == 5 and all([1 for c in patterns[1] if c in opset]):
			patterns[3] = opset
	return patterns


#  000
# 1   2
# 1   2
#  333
# 4   5
# 4   5
#  666


def print_letters(letters: dict) -> None:
	print(f' {letters[0] * 3}')
	for _ in range(2):
		print(f'{letters[1]}  {letters[2]}')
	print(f' {letters[3] * 3}')
	for _ in range(2):
		print(f'{letters[4]}  {letters[5]}')
	print(f' {letters[6] * 3}')


def set_hard(row: str, patterns: dict) -> dict:
	segments = {x: '' for x in range(7)}
	segments[0] = list(patterns[7] - patterns[1])[0]
	segments[6] = list(patterns[3] - patterns[4] - {segments[0]})[0]
	one_or_three = patterns[4] - patterns[1]
	patterns[9] = patterns[4].union({segments[0], segments[6]})
	segments[4] = list(patterns[8] - patterns[9])[0]
	segments[3] = list(patterns[3] - patterns[7] - {segments[6]})[0]
	patterns[0] = patterns[8] - {segments[3]}
	ops = row.replace(' | ', ' ').split(' ')
	for op in ops:
		opset = set(op)
		if len(opset) == 6 and opset != patterns[9] and opset != patterns[0]:
			patterns[6] = opset
			segments[2] = list(patterns[8] - patterns[6])[0]
			segments[5] = list(patterns[1] - {segments[2]})[0]
			print(f'patterns6 = {patterns[6]}, segments2 = {segments[2]}')
			break

	segments[1] = list(patterns[4] - patterns[1] - {segments[3]})[0]
	patterns[2] = patterns[8] - {segments[1]} - {segments[5]}
	print(f'patterns5 would be {patterns[8]} - {segments[2]} - {segments[4]}')
	patterns[5] = patterns[8] - {segments[2]} - {segments[4]}
	print(f'patterns[5]={patterns[5]}')
	# print_letters(letters)
	print(f'segments={segments}')
	print(f'patterns={patterns}')
	return patterns


def reverse_dict(patterns: dict) -> dict:
	return {str(patterns[key]): key for key in patterns}


def decode(row: str, patterns: dict) -> int:
	outcome = 0
	_, output = row.split(' | ')
	output = output.split(' ')
	value = str()
	for item in output:
		print(f'checking {item}')
		for kv in patterns.items():
			if set(item) == kv[1]:
				value += str(kv[0])
				print(f'value now is {value}')
			else:
				print(f'{set(item)} != {kv[1]}')
	# print(value)
	outcome += int(value)
	return outcome


def part2(rows: list[str]):
	outcome = 0
	for row in rows:
		patterns = set_easy(row)
		print(f'after ez: patterns={patterns}')
		patterns = set_hard(row, patterns)
		outcome += decode(row, patterns)
	return outcome


lines = open("input.txt").read().splitlines()
# print(f'Part1: {part1(lines)}')
print(f'Part2: {part2(lines)}')
