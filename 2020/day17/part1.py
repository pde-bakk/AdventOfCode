from collections import defaultdict
import copy


def alive_cubes(finalgrid):
	total = 0
	for zz in finalgrid:
		for yy in finalgrid[zz]:
			total += yy.count('#')
	return total


def find_neighbours():
	total = 0
	for checkz in range(z - 1, z + 2):
		if checkz not in grid:
			continue
		for checky in range(y - 1, y + 2):
			if checky < 0 or checky >= len(grid[checkz]):
				continue
			start, end = max(0, x - 1), min(x + 2, len(grid[checkz][checky]))
			count = grid[checkz][checky].count('#', start, end)
			total += count
	if grid[z][y][x] == '#':
		total -= 1
	return total


def new_zealand(width, height):
	return [width * '.' for u in range(height)]


def expand_board(maingrid):
	for lvl in sorted(maingrid):
		for yy, row in enumerate(maingrid[lvl]):
			maingrid[lvl][yy] = '.' + row + '.'
		emptyline = len(maingrid[lvl][0]) * '.'
		maingrid[lvl] = [emptyline] + maingrid[lvl] + [emptyline]
	maingrid[max(maingrid, key=int) + 1] = new_zealand(len(maingrid[0][0]), len(maingrid[0]))
	maingrid[min(maingrid, key=int) - 1] = new_zealand(len(maingrid[0][0]), len(maingrid[0]))
	return maingrid


def trim_edges(maingrid):
	do_again = False
	if all(all(row[0] == '.' for row in maingrid[lvl]) for lvl in maingrid):
		do_again = True
		for lvl in maingrid:
			for rr, row in enumerate(maingrid[lvl]):
				maingrid[lvl][rr] = row[1:]
	if all(all(row[-1] == '.' for row in maingrid[lvl]) for lvl in maingrid):
		do_again = True
		for lvl in maingrid:
			for rr, row in enumerate(maingrid[lvl]):
				maingrid[lvl][rr] = row[:-1]
	if all(len(set(maingrid[lvl][0])) == 1 for lvl in maingrid):
		do_again = True
		for lvl in maingrid:
			maingrid[lvl].pop(0)
	if all(len(set(maingrid[lvl][-1])) == 1 for lvl in maingrid):
		do_again = True
		for lvl in maingrid:
			maingrid[lvl].pop()
	minlayer, maxlayer = min(maingrid, key=int), max(maingrid, key=int)
	if all(len(set(row)) == 1 for row in maingrid[minlayer]):
		do_again = True
		maingrid.pop(minlayer)
	if all(len(set(row)) == 1 for row in maingrid[maxlayer]):
		do_again = True
		maingrid.pop(maxlayer)
	if do_again:
		return trim_edges(maingrid)
	else:
		return maingrid


file = open('input', 'r').read().split('\n')
newgrid = grid = defaultdict(list)
grid[0] = list(file)
newgrid[0] = list(file)

for i in range(6):
	newgrid = expand_board(newgrid)
	grid = copy.deepcopy(newgrid)
	for z in grid:
		for y, r in enumerate(grid[z]):
			for x, c in enumerate(r):
				if c == '.' and find_neighbours() == 3:
					newgrid[z][y] = newgrid[z][y][:x] + '#' + newgrid[z][y][x+1:]
				elif c == '#' and find_neighbours() not in range(2, 4):
					newgrid[z][y] = newgrid[z][y][:x] + '.' + newgrid[z][y][x+1:]
	newgrid = trim_edges(newgrid)

for blaz in sorted(newgrid):
	print(f'z={blaz}')
	for g in newgrid[blaz]:
		print(g)
	print('')
print(f'part 1 has {alive_cubes(newgrid)} cubes')

