from math import sqrt
import numpy as np


def get_rotation(item: np.ndarray) -> np.ndarray:
	for _ in range(2):  # Flips
		for _ in range(4):  # Rotations
			yield item
			item = np.rot90(item)
		item = np.flip(item, axis=0)


def build_solution(grid: dict[int, np.ndarray]):
	for t in grid:
		matches = 0
		for rot in get_rotation(grid[t]):
			# print(f'{t}\n{item}')
			for other in grid:
				if other == t:
					continue
				for other_rot in get_rotation(grid[other]):
					# print(f'rot has type {type(rot)}, other_rot has type {type(other_rot)}')
					matches += int(np.array_equal(rot[0], other_rot[-1]))
					matches += int(np.array_equal(rot[-1], other_rot[0]))
					matches += int(np.array_equal(rot[:, 0], other_rot[:, -1]))
					matches += int(np.array_equal(rot[:, -1], other_rot[:, 0]))
		print(f'{t} has {matches} matches')
	pass


tiles = open('input.txt').read().split('\n\n')
size = int(sqrt(len(tiles)))
solution = np.zeros(shape=(size, size), dtype=np.uint16)
images = {}
for tile in tiles:
	tile_nb, array = tile.split(sep='\n', maxsplit=1)
	nb = int(tile_nb.split(' ')[1].rstrip(':'))
	arr = np.zeros(shape=(10, 10), dtype=np.uint8)
	for y, row in enumerate(array.split('\n')):
		for x, pixel in enumerate(row):
			arr[y][x] = int(pixel == '#')
	images[nb] = arr

build_solution(images)
