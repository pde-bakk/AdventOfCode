import copy


class Tile:
	WHITE = 0
	BLACK = 1


d = dict()
myinput = [x.replace('e', 'e ').replace('w', 'w ').split() for x in open('input', 'r').read().splitlines() if x != '']
blacktiles = 0
for line in myinput:
	locx, locy = 0, 0
	for move in line:
		mult = 1
		if 'n' in move or 's' in move:
			mult = 0.5
			if 'n' in move:
				locy += 1
			else:
				locy -= 1
		if 'e' in move:
			locx += mult * 1
		else:
			locx -= mult * 1
	if (locx, locy) in d:
		del d[locx, locy]
	else:
		d[locx, locy] = Tile.BLACK
for key in d:
	blacktiles += d[key]
print(f'-- Part 1: {blacktiles} black tiles --')
d2 = dict()

for day in range(100):
	d2.clear()
	whites = set()
	for key in d:
		x, y = key
		neigbours = [(x-1, y), (x+1, y), (x-0.5, y-1), (x-0.5, y+1), (x+0.5, y-1), (x+0.5, y+1)]
		blackneighours = 0
		for n in neigbours:
			if n in d:
				blackneighours += bool(n in d)
			else:
				whites.add(n)
		if 0 < blackneighours < 3:
			d2[key] = d[key]
	for whitetile in whites:
		x, y = whitetile
		neigbours = [(x-1, y), (x+1, y), (x-0.5, y-1), (x-0.5, y+1), (x+0.5, y-1), (x+0.5, y+1)]
		blackneighours = 0
		for n in neigbours:
			blackneighours += bool(n in d)
		if blackneighours == 2:
			d2[whitetile] = Tile.BLACK
	d.clear()
	whites.clear()
	d = copy.deepcopy(d2)
print(f'-- Part 2: {len(d)} --')
