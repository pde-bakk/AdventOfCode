def setup_rocks(rows: list[str]) -> set:
	rocks = set()
	for row in rows:
		coords = [tuple(map(int, x.split(','))) for x in row.split(' -> ')]
		for (x1, y1), (x2, y2) in zip(coords, coords[1:]):
			x1, x2 = sorted([x1, x2])
			y1, y2 = sorted([y1, y2])
			for y in range(y1, y2 + 1):
				for x in range(x1, x2 + 1):
					rocks.add((x, y))
	return rocks


def print_example(rocks: set[tuple]) -> None:
	for y in range(10):
		s = ['#' if (x, y) in rocks else '.' for x in range(494, 504)]
		print(''.join(s))


def day14(lines: list[str], part: int = 1) -> None:
	rocks = setup_rocks(lines)
	rocks_amount = len(rocks)
	highest = max([y for x, y in rocks])

	sand_source, alive = (500, 0), True
	while alive:
		old_sand_pos = None
		sand_pos = sand_source
		while sand_pos != old_sand_pos:
			old_sand_pos = tuple(sand_pos)
			x, y = sand_pos
			down, downleft, downright = (x, y + 1), (x - 1, y + 1), (x + 1, y + 1)
			if down not in rocks:
				sand_pos = down
			elif downleft not in rocks:
				sand_pos = downleft
			elif downright not in rocks:
				sand_pos = downright
			if part == 1 and sand_pos[1] >= highest:
				alive = False
				break
			elif part == 2 and sand_pos[1] >= highest + 1:
				break
		if alive:
			rocks.add(sand_pos)
			if sand_pos == sand_source:
				break

	# print_example(rocks)
	print(f'Part {part}:', len(rocks) - rocks_amount)


if __name__ == '__main__':
	with open('input.txt', 'r') as f:
		aoc_input = f.read().splitlines()
	day14(aoc_input, part=1)
	day14(aoc_input, part=2)
