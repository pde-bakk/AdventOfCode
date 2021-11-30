from itertools import groupby


def part1(val: str) -> int:
	for _ in range(50):
		groups = groupby(val)
		result = [(label, sum(1 for _ in group)) for label, group in groups]
		val = ''.join([''.join(map(str, x[::-1])) for x in result])
	return len(val)


print(part1('1113122113'))
