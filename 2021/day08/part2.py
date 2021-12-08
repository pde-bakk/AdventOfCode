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


def set_hard(items: list[str], patterns: dict) -> dict:
	segments = {x: '' for x in range(7)}
	for item in items:
		if len(item) == 6:  # Item is one of patterns 0, 6, 9
			eightdiff = list(patterns[8] - set(item))[0]
			if list(eightdiff)[0] in patterns[1]:  # Item is pattern 6, eightdiff is segment 2
				patterns[6] = set(item)
				segments[2] = eightdiff
			elif eightdiff in patterns[4]:  # eightdiff is segment 3, item is pattern 0
				patterns[0] = set(item)
				segments[3] = eightdiff
			else:  # eightdiff is segment 4, item is pattern 9
				patterns[9] = set(item)
				segments[4] = eightdiff

	for item in items:
		if len(item) in [2, 3, 4, 7]:
			continue
		elif len(item) == 5:
			eightdiff = list(patterns[8] - set(item))
			if eightdiff[0] not in patterns[1] and eightdiff[1] not in patterns[1]:  # Item=3, segments are 1 and 4
				patterns[3] = set(item)
			else:
				sixdiff = list(patterns[6] - set(item))
				if len(sixdiff) == 1:
					patterns[5] = set(item)
				else:
					patterns[2] = set(item)
	return patterns


def decode(items: list[str], patterns: dict) -> int:
	res = 0
	value = str()
	for item in items:
		for kv in patterns.items():
			if set(item) == kv[1]:
				value += str(kv[0])
	res += int(value)
	return res


def part2(rows: list[str]):
	outcome = 0
	for row in rows:
		firsts, seconds = row.split(' | ')
		firsts, seconds = firsts.split(), seconds.split()
		patterns = set_easy(firsts)
		patterns = set_hard(firsts, patterns)
		outcome += decode(seconds, patterns)
	return outcome


if __name__ == '__main__':
	lines = open("input.txt").read().splitlines()
	print(f'Part2: {part2(lines)}')
