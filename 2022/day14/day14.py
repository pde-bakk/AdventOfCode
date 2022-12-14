import copy


with open('input.txt', 'r') as f:
	lines = f.read().splitlines()
rocks = set()
for line in lines:
	coords = [tuple(map(int, x.split(','))) for x in line.split(' -> ')]
	print(coords)
	for i, coord in enumerate(coords[1:], start=1):
		a, b = min(coord, coords[i - 1]), max(coord, coords[i - 1])
		print(f'min={a}, max={b}')
		if a[0] == b[0]:  # x same
			for y in range(a[1], b[1] + 1):
				rocks.add((a[0], y))
		elif a[1] == b[1]:
			for x in range(a[0], b[0] + 1):
				rocks.add((x, b[1]))
		else:
			raise NotImplementedError

for y in range(10):
	s = ['#' if (x, y) in rocks else '.' for x in range(494, 504)]
	print(''.join(s))
rocks_amount = len(rocks)
highest = max([y for x, y in rocks])
print(f'There are {rocks_amount} rocks and the highest y value is {highest}')
old_rocks = copy.deepcopy(rocks)
alive = True
while alive:
	old_sand_pos = None
	sand_pos = (500, 0)
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
		if sand_pos[1] >= highest:
			alive = False
			break
	if alive:
		rocks.add(sand_pos)
		print(f'just added {sand_pos}')

for y in range(10):
	s = ['#' if (x, y) in rocks else '.' for x in range(494, 504)]
	print(''.join(s))
highest = min([y for x, y in rocks])
print(len(rocks))
print(f'Part 1:', len(rocks) - rocks_amount)
