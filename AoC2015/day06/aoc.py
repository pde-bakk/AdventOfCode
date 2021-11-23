import re
from typing import List


def part1(rows: List[str]) -> int:
	lights = [[False] * 1000 for _ in range(1000)]
	for row in rows:
		if not row:
			break
		x1, y1, x2, y2 = [int(s) for s in re.findall(r'\b\d+\b', row)]
		for y in range(y1, y2 + 1):
			for x in range(x1, x2 + 1):
				if 'turn on' in row:
					lights[y][x] = True
				elif 'turn off' in row:
					lights[y][x] = False
				elif 'toggle' in row:
					lights[y][x] = not lights[y][x]
	return sum(sum(light for light in row) for row in lights)


def part2(rows: List[str]) -> int:
	lights = [[0] * 1000 for _ in range(1000)]
	for row in rows:
		if not row:
			break
		x1, y1, x2, y2 = [int(s) for s in re.findall(r'\b\d+\b', row)]
		for y in range(y1, y2 + 1):
			for x in range(x1, x2 + 1):
				if 'turn on' in row:
					lights[y][x] += 1
				elif 'turn off' in row:
					lights[y][x] = max(0, lights[y][x] - 1)
				elif 'toggle' in row:
					lights[y][x] += 2
	return sum(sum(light for light in row) for row in lights)


assert part1(['turn on 0,0 through 999,0']) == 1000
assert part1(['toggle 499,499 through 500,500']) == 4
input_rows = open('input.txt', 'r').read().split('\n')
print(part1(input_rows))

# Part 2

print(part2(input_rows))
