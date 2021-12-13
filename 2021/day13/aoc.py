import numpy as np


def day13(matrix, part) -> int:
	for fold in folds:
		if fold[0] == 'y':
			fy = fold[1]
			for y in range(1, ymax):
				if fy + y >= matrix.shape[0]:
					break
				matrix[fy - y] |= matrix[fy + y]
			matrix = matrix[:fy]
		elif fold[0] == 'x':
			fx = fold[1]
			for x in range(1, xmax):
				if fx + x >= matrix.shape[1]:
					break
				matrix[:, fx - x] |= matrix[:, fx + x]
			matrix = matrix[:, 0:fx]
		if part == 1:
			break
	if part == 2:
		for row in matrix:
			for c in row:
				if c == 0:
					print(' ', end='')
				else:
					print('#', end='')
			print()
	return matrix.sum()


dots, fold_input = open('input.txt').read().split('\n\n')
dots = [[int(x) for x in row.split(',')] for row in dots.split('\n')]
folds = [(f[0][-1], int(f[1])) for row in fold_input.split('\n') if (f := row.split('='))]
xmax, ymax = 0, 0
for dot in dots:
	xmax = max(xmax, dot[0] + 1)
	ymax = max(ymax, dot[1] + 1)

grid = np.zeros(shape=(ymax, xmax), dtype=np.uint8)
for dot in dots:
	grid[dot[1]][dot[0]] = 1

print(f'Part1: {day13(grid, part=1)}')
print(f'Part2: {day13(grid, part=2)}')
