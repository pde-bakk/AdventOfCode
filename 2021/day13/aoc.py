import numpy as np


def part1(matrix):
	print()
	for f in folds:
		if f[0] == 'y':
			for y in range(size):
				print(f'f = {f}')
				if f[1] + y >= matrix.shape[1]:
					continue
				matrix[f[0] - y] |= matrix[f[0] + y]
				for ye in range(y, size):
					matrix = np.delete(matrix, ye)
	print(matrix)


dots, fold_input = open('input.txt').read().split('\n\n')
dots = [[int(x) for x in row.split(',')] for row in dots.split('\n')]
folds = []
for row in fold_input.split('\n'):
	if not row:
		continue
	r = row.split('=')
	folds += tuple([r[0][-1], int(r[1])])

size = 15
print(size)
grid = np.zeros(shape=(size, size), dtype=np.uint8)
for dot in dots:
	grid[dot[1]][dot[0]] = 1
print(dots)
print(folds)
for g in grid:
	print(g)

print(f'here')
part1(grid)
