import re


def get_next(yy: int, xx: int) -> tuple[int, int]:
	if current_dir[0]:
		new_y = yy + current_dir[0]
		if new_y == -1 or new_y == len(tiles) or xx >= len(tiles[new_y]) or tiles[new_y][xx].isspace():
			new_y = yy
			while xx < len(tiles[new_y]) and not tiles[new_y][xx].isspace():
				new_new_y = new_y - current_dir[0]
				if 0 <= new_new_y < len(tiles) and xx < len(tiles[new_new_y]) and not tiles[new_new_y][xx].isspace():
					new_y = new_new_y
				else:
					break
		# elif
		return new_y, xx
	else:
		new_x = xx + current_dir[1]
		if new_x == -1:
			new_x = len(tiles[yy]) - 1
		elif new_x == len(tiles[yy]):
			new_x = 0
		return yy, new_x


directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # (y, x)
current = 0
y, x = 0, 0
with open('input.txt', 'r') as f:
	tiles, path = f.read().split('\n\n')
	tiles = tiles.splitlines()
	ints = list(map(int, re.findall(r'\d+', path)))
	rotations = re.findall(r'[A-Z]', path)
	path = [val for pair in zip(ints, rotations) for val in pair]
# print(tiles)
print(len(tiles))
x = tiles[0].index('.')
for instr in path:
	current_dir = directions[current]
	if isinstance(instr, int):
		print(f'{instr=}, {current_dir=}')
		for i in range(instr):
			next_y, next_x = get_next(y, x)
			print(f'{next_y=}, {next_x=}')

			if tiles[next_y][next_x] == '#':
				break
			y, x = next_y, next_x
			# print(f'MOVING TO {tiles[y][x]}')
		print(f'Moved to {y, x}')
	elif instr in 'LR':
		if instr == 'L':
			current -= 1
		else:
			current += 1
		current = current % len(directions)
	else:
		raise NotImplementedError

part_1 = [1000 * (y + 1), 4 * (x + 1), current]
print(sum(part_1))
