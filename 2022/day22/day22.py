import re


directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # (y, x)
current = 0
with open('input.txt', 'r') as f:
	tiles, path = f.read().split('\n\n')
	tiles_lines = tiles.splitlines()
	tiles = {}
	for y, line in enumerate(tiles_lines):
		for x, item in enumerate(line):
			if item in '.#':
				tiles[(y, x)] = item
	ints = list(map(int, re.findall(r'\d+', path)))
	rotations = re.findall(r'[A-Z]', path)
	path = [val for pair in zip(ints, rotations) for val in pair]
	if ints[-1] != path[-1]:
		path.append(ints[-1])

print(len(tiles))
y, x = min(tiles.keys())
for instr in path:
	dy, dx = directions[current]
	if isinstance(instr, int):
		for _ in range(instr):
			next_y, next_x = y + dy, x + dx
			new_tile = tiles.get((next_y, next_x))
			if new_tile is None:  # Wrap around
				nny, nnx = y, x
				while (nny, nnx) in tiles:
					next_y, next_x = nny, nnx
					nny -= dy
					nnx -= dx
				new_tile = tiles.get((next_y, next_x))
			if new_tile == '#':  # Hit the wall
				break
			y, x = next_y, next_x
			# print(f'MOVING TO {tiles[y][x]}')
		# print(f'Moved to {y, x}')
	elif instr in 'LR':
		if instr == 'L':
			current -= 1
		else:
			current += 1
		current = current % len(directions)
	else:
		raise NotImplementedError

part_1 = [1000 * (y + 1), 4 * (x + 1), current]
print(sum(part_1), y, x, current)
