def print_octos(listy, step: int = 0):
	if step == 0:
		print('Before any steps:')
	else:
		print(f'After step {step}')
	for line in listy:
		print(line)


def day11(octos: list[list[int]]):
	print_octos(octos)

	def flash(yy: int, xx: int) -> int:
		neighbours = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
		octos[yy][xx] = -1
		octoflash = 1

		for n in neighbours:
			ny, nx = n[0] + yy, n[1] + xx
			if ny == -1 or nx == -1 or ny == len(octos) or nx == len(octos[ny]):
				continue
			if octos[ny][nx] == -1:
				continue
			octos[ny][nx] += 1
			if octos[ny][nx] > 9:
				octoflash += flash(ny, nx)
		return octoflash

	flashes = 0
	for step in range(1000):
		stepflashes = 0
		# Increment energy levels of all octopi
		for y, row in enumerate(octos):
			for x, octo in enumerate(row):
				octos[y][x] += 1
		# Flash!
		for y, row in enumerate(octos):
			for x, octo in enumerate(row):
				if octos[y][x] > 9:
					stepflashes += flash(y, x)
		flashes += stepflashes

		# reset energy levels
		for y, row in enumerate(octos):
			for x, octo in enumerate(row):
				if octos[y][x] == -1:
					octos[y][x] = 0
		print_octos(octos, step)
		if stepflashes == len(octos) * len(octos[0]):
			print(f'Part2: {step + 1}')
		if step == 100:
			print(f'Part1: {flashes}')


grid = [[int(x) for x in line] for line in open('input.txt').read().splitlines()]
day11(grid)
