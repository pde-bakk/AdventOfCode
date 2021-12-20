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


def get_string(pos: tuple, img: set[tuple], algo: list[int]):
	res = 0
	for n in get_neighbours():
		neighbour_pos = tuple(map(operator.add, pos, n))
		res = (res << 1) + int(neighbour_pos in img)
	return algo[res]


def enhance(algo: list[int], img: set[tuple], steps: int):
	for step in range(steps):
		new_image = set()
		new_checkings = copy.deepcopy(img)
		for pix in img:
			for n in get_neighbours():
				new_checkings.add(tuple(map(operator.add, pix, n)))
		for pix in new_checkings:
			if get_string(pix, img, algo):
				new_image.add(pix)
		# print(sorted(list(new_image)))
		print(len(new_image))
		img = copy.deepcopy(new_image)
		# break
	return img


def main(filename: str) -> tuple:
	algo, img, minmax = parse(filename)
	img = enhance(algo, img, 2)
	print(f'len img = {len(img)}')
	return len(img), 0


if __name__ == '__main__':
	example_outcome = main('example.txt')
	assert example_outcome[0] == 35
	# assert example_outcome[1] == 3621
	real_outcome = main('input.txt')
	print(f'Part1: {real_outcome[0]}')
	print(f'Part2: {real_outcome[1]}')
