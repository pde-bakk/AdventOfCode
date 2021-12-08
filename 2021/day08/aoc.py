def part1(rows: list[str]) -> int:
	total = 0
	for row in rows:
		_, output = row.split(' | ')
		output = output.split(' ')
		for item in output:
			total += int(len(set(item)) in (2, 3, 4, 7))
	return total


def set_easy(items: list[str]) -> dict:
	patterns = {x: set() for x in range(10)}
	for item in items:
		opset = set(item)
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
		elif setlen == 5 and all([c in opset for c in patterns[7]]):
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


# yet to do 2, 5, 6, 9

def set_hard(items: list[str], patterns: dict) -> dict:
	segments = {x: '' for x in range(7)}
	print(f'4-3={patterns[4] - patterns[3]}')
	print(f'3-4={patterns[3] - patterns[4]}')
	print(f'items is {items}')
	for item in items:
		if len(item) in [2, 3, 4, 7]:
			continue
		# print(f'item={item}')
		if len(item) == 6:  # Item is one of patterns 0, 6, 9
			eightdiff = list(patterns[8] - set(item))[0]
			if list(eightdiff)[0] in patterns[1]:  # Item is pattern 6, eightdiff is segment 2
				# print(f'Found pattern 6 in item {item}, eightdiff = {eightdiff} (segment 2)')
				patterns[6] = set(item)
				segments[2] = eightdiff
			elif eightdiff in patterns[4]:  # eightdiff is segment 3, item is pattern 0
				# print(f'Found pattern 0 in item {item}, eightdiff = {eightdiff} (segment 3)')
				patterns[0] = set(item)
				segments[3] = eightdiff
			else:  # eightdiff is segment 4, item is pattern 9
				# print(f'Found pattern 9 in item {item}, eightdiff = {eightdiff} (segment 4)')
				patterns[9] = set(item)
				segments[4] = eightdiff

	for item in items:
		if len(item) in [2, 3, 4, 7]:
			continue
		elif len(item) == 5:
			eightdiff = list(patterns[8] - set(item))
			print(f'{item}, eightdiff is {eightdiff}')
			if eightdiff[0] not in patterns[1] and eightdiff[1] not in patterns[1]:  # Item=3, segments are 1 and 4
				print(f'Found pattern 3 in item {item}, eightdiff={eightdiff}')
				patterns[3] = set(item)
			else:
				sixdiff = list(patterns[6] - set(item))
				print(f'patterns[6] = {patterns[6]}, sixdiff = {sixdiff}')
				if len(sixdiff) == 1:
					patterns[5] = set(item)
				else:
					patterns[2] = set(item)
	print(f'segments={segments}')
	print(f'patterns={patterns}')
	return patterns


def reverse_dict(patterns: dict) -> dict:
	return {str(patterns[key]): key for key in patterns}


def decode(items: list[str], patterns: dict) -> int:
	outcome = 0
	value = str()
	for item in items:
		print(f'checking {item}')
		for kv in patterns.items():
			if set(item) == kv[1]:
				value += str(kv[0])
				print(f'value now is {value}')
			# else:
			# 	print(f'{set(item)} != {kv[1]}')
	print(f'adding {value}')
	outcome += int(value)
	return outcome


def part2(rows: list[str]):
	outcome = 0
	for i, row in enumerate(rows):
		patterns = {}
		# if i != 6:
		# 	continue
		print(f'checking row {i}')
		firsts, seconds = row.split(' | ')
		patterns = set_easy(firsts.split())
		print(f'after ez: patterns={patterns}')
		patterns = set_hard(firsts.split(), patterns)
		outcome += decode(seconds.split(), patterns)
	return outcome


lines = open("input.txt").read().splitlines()
# print(f'Part1: {part1(lines)}')
print(f'Part2: {part2(lines)}')
