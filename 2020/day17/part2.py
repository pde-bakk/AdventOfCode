from collections import defaultdict
import copy
#1792

def alive_cubes(finalgrid):
	total = 0
	for ww in sorted(finalgrid):
		for zz in sorted(finalgrid[ww]):
			for yy in finalgrid[ww][zz]:
				total += yy.count('#')
	return total


def find_neighbours():
	total = 0
	for checkw in range(w - 1, w + 2):
		if checkw not in grid:
			continue
		for checkz in range(z - 1, z + 2):
			if checkz not in grid[checkw]:
				continue
			for checky in range(y - 1, y + 2):
				if checky < 0 or checky >= len(grid[checkw][checkz]):
					continue
				start, end = max(0, x - 1), min(x + 2, len(grid[checkw][checkz][checky]))
				total += grid[checkw][checkz][checky].count('#', start, end)
	if grid[w][z][y][x] == '#':
		total -= 1
	return total


def expand_board(maingrid):
	for wlvl in sorted(maingrid):
		for lvl in maingrid[wlvl]:
			for yy, row in enumerate(maingrid[wlvl][lvl]):
				maingrid[wlvl][lvl][yy] = '.' + row + '.'
			emptyline = len(maingrid[wlvl][lvl][0]) * '.'
			maingrid[wlvl][lvl] = [emptyline] + maingrid[wlvl][lvl] + [emptyline]
		maingrid[wlvl][max(maingrid[wlvl], key=int) + 1] = [len(maingrid[wlvl][lvl][0]) * '.' for u in range(len(maingrid[wlvl][lvl]))]
		maingrid[wlvl][min(maingrid[wlvl], key=int) - 1] = [len(maingrid[wlvl][lvl][0]) * '.' for u in range(len(maingrid[wlvl][lvl]))]
	maingrid[max(maingrid, key=int) + 1] = [len(maingrid[lvl][0]) * '.' for u in range(len(maingrid[lvl]))]
	maingrid[min(maingrid, key=int) - 1] = [len(maingrid[lvl][0]) * '.' for u in range(len(maingrid[lvl]))]
	return maingrid


def trim_edges(maingrid):
	do_again = False
	for ww in maingrid:
		print(f'ww ({ww}) type is {type(ww)}, lvl type is {type(maingrid[ww][0])} ({maingrid[ww][0]})')
		if all(all(row[0] == '.' for row in maingrid[ww][lvl]) for lvl in maingrid[ww]):
			do_again = True
			for lvl in maingrid[ww]:
				for rr, row in enumerate(maingrid[ww][lvl]):
					maingrid[ww][lvl][rr] = row[1:]
		if all(all(row[-1] == '.' for row in maingrid[ww][lvl]) for lvl in maingrid[ww]):
			do_again = True
			for lvl in maingrid[ww]:
				for rr, row in enumerate(maingrid[ww][lvl]):
					maingrid[ww][lvl][rr] = row[:-1]
		if all(len(set(maingrid[ww][lvl][0])) == 1 for lvl in maingrid[ww]):
			do_again = True
			for lvl in maingrid[ww]:
				maingrid[ww][lvl].pop(0)
		if all(len(set(maingrid[ww][lvl][-1])) == 1 for lvl in maingrid[ww]):
			do_again = True
			for lvl in maingrid[ww]:
				maingrid[ww][lvl].pop()
		minlayer, maxlayer = min(maingrid[ww], key=int), max(maingrid[ww], key=int)
		if all(len(set(row)) == 1 for row in maingrid[ww][minlayer]):
			do_again = True
			maingrid[ww].pop(minlayer)
		if all(len(set(row)) == 1 for row in maingrid[ww][maxlayer]):
			do_again = True
			maingrid[ww].pop(maxlayer)
	wminlayer, wmaxlayer = min(maingrid, key=int), max(maingrid, key=int)
	if all(all(len(set(row)) == 1 for row in zdim) for zdim in maingrid[wminlayer]):
		do_again = True
		maingrid.pop(wminlayer)
	if all(all(len(set(row)) == 1 for row in zdim) for zdim in maingrid[wmaxlayer]):
		do_again = True
		maingrid.pop(wmaxlayer)
	if do_again:
		return trim_edges(maingrid)
	else:
		return maingrid


file = open('input', 'r').read().split('\n')
newgrid = defaultdict(list)
w, z = 0, 0
newgrid[w] = defaultdict(list)
newgrid[w][z] = list(file)

for i in range(6):
	newgrid = expand_board(newgrid)
	grid = copy.deepcopy(newgrid)
	for w in grid:
		for z, zzz in enumerate(grid[w]):
			for y, yyy in enumerate(grid[w][z]):
				for x, c in enumerate(yyy):
					if c == '.' and find_neighbours() == 3:
						newgrid[w][z][y] = newgrid[w][z][y][:x] + '#' + newgrid[w][z][y][x+1:]
					elif c == '#' and find_neighbours() not in range(2, 4):
						newgrid[w][z][y] = newgrid[w][z][y][:x] + '.' + newgrid[w][z][y][x+1:]
	newgrid = trim_edges(newgrid)

for blaw in sorted(newgrid):
	for blaz in newgrid[blaw]:
		print(f'z={blaz}, w={blaw}')
		for g in newgrid[blaw][blaz]:
			print(g)
		print('')
print(f'part 2 has {alive_cubes(newgrid)} cubes')

