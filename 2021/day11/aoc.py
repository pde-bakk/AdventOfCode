from copy import deepcopy


def print_octos(listy, step: int=0):
	if step == 0:
		print('Before any steps:')
	else:
		print(f'After step {step}')
	for line in listy:
		print(line)


def part1(curr: list[list[int]]) -> int:
	print_octos(curr)

	def flash(yy: int, xx: int) -> int:
		neighbours = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
		curr[yy][xx] = -1
		flashes = 1

		for n in neighbours:
			ny, nx = n[0] + yy, n[1] + xx
			if ny == -1 or nx == -1 or ny == len(curr) or nx == len(curr[ny]):
				continue
			if curr[ny][nx] == -1:
				continue
			curr[ny][nx] += 1
			# print(f'n={n}, neighbour={curr[n[0]][n[1]]}')
			if curr[ny][nx] > 9:
				flashes += flash(ny, nx)
		return flashes

	# newstate = deepcopy(curr)
	flashes = 0
	for step in range(1000):
		stepflashes = 0
		for y, row in enumerate(curr):
			for x, octo in enumerate(row):
				curr[y][x] += 1
		for y, row in enumerate(curr):
			for x, octo in enumerate(row):
				if curr[y][x] > 9:
					stepflashes += flash(y, x)
		flashes += stepflashes
		# reset energy levels
		for y, row in enumerate(curr):
			for x, octo in enumerate(row):
				if curr[y][x] == -1:
					curr[y][x] = 0
		print_octos(curr, step)
		if stepflashes == len(curr) * len(curr[0]):
			return step + 1
	return flashes


octos = [[int(x) for x in line] for line in open('input.txt').read().splitlines()]
print(octos)
print(f'Part1: {part1(octos)}')
