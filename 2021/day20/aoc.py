import numpy as np
import operator
import copy


#	.......
#	.0..#..
#	.#.....
#	.##..#.
#	...#...
#	...###.
#	.......


def get_neighbours():
	for _y in [-1, 0, 1]:
		for _x in [-1, 0, 1]:
			yield _y, _x


def parse(filename: str) -> tuple[list[int], set[tuple], tuple[int, int]]:
	algo, image = open(filename).read().split('\n\n')
	algo = [int(c == '#') for c in algo.replace('\n', '')]
	img = set()
	maxi = 0

	for y, row in enumerate(image.splitlines()):
		maxi = len(row)
		for x, pixel in enumerate(row):
			if pixel == '#':
				img.add((y, x))
	return algo, img, (0, maxi)


def get_string(pos: tuple, img: set[tuple], algo: list[int], xmin, xmax, ymin, ymax, step):
	res = 0
	for n in get_neighbours():
		neighbour_pos = tuple(map(operator.add, pos, n))
		res = res << 1
		if ymin <= neighbour_pos[0] <= ymax and xmin <= neighbour_pos[1] <= xmax:
			res += int(neighbour_pos in img)
		else:
			res += int(step % 2)
	return algo[res]


def enhance(algo: list[int], img: set[tuple], steps: int):
	for step in range(steps):
		xmin, xmax, ymin, ymax = 0, 0, 0, 0
		for x, y in img:
			xmin, xmax = min(x, xmin), max(x, xmax)
			ymin, ymax = min(y, ymin), max(y, ymax)

		new_image = set()
		for y in range(ymin - 1, ymax + 2):
			for x in range(xmin - 1, xmax + 2):
				if get_string((y, x), img, algo, xmin, xmax, ymin, ymax, step):
					new_image.add((y, x))
		img = copy.deepcopy(new_image)
	return img


def main(filename: str) -> tuple:
	algo, img, minmax = parse(filename)
	img = enhance(algo, img, 2)
	p1 = len(img)
	p2 = len(enhance(algo, img, 48))
	print(f'len img = {len(img)}')
	return p1, p2


if __name__ == '__main__':
	example_outcome = main('example.txt')
	# assert example_outcome[0] == 35
	# assert example_outcome[1] == 3621
	real_outcome = main('input.txt')
	print(f'Part1: {real_outcome[0]}')
	print(f'Part2: {real_outcome[1]}')
