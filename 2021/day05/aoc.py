import numpy as np


def day05(rows: list[str], part2: bool):
	floor = np.zeros(shape=(1000, 1000), dtype=np.uint16)
	for row in rows:
		start, end = [list(map(int, x.split(','))) for x in row.split(' -> ')]
		if start[0] == end[0]:
			begin, end = min(start[1], end[1]), max(start[1], end[1])
			for i in range(begin, end + 1):
				floor[i][start[0]] += 1
		elif start[1] == end[1]:
			begin, end = min(start[0], end[0]), max(start[0], end[0])
			for i in range(begin, end + 1):
				floor[start[1]][i] += 1
		elif part2:  # diagonal, not for part 1
			while True:
				floor[start[1]][start[0]] += 1
				if start == end:
					break
				start[0] += 1 if end[0] > start[0] else -1
				start[1] += 1 if end[1] > start[1] else -1
	return len([1 for x in np.ndenumerate(floor) if x[1] >= 2])


lines = open("input.txt").read().splitlines()
print(f'Part1: {day05(lines, False)}')
# print(f'Part2: {day05(lines, True)}')
