def nbadjacencies():
	ret = 0
	directions = (-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)
	for dx, dy in directions:
		i, j = x - dx, y - dy
		while i in range(0, len(rows[y]) -1) and j in range(0, len(rows) - 1):
			if rows[j][i] == '#':
				ret += 1
	for j in range(max(0, y - 1), min(y + 1, len(rows) - 1) + 1):
		for i in range(max(0, x - 1), min(x + 1, len(rows[y]) - 1) + 1):
			# print("checking for adjancencies, xy = {},{}, ij = {}, {}".format(x, y, i, j))
			if i == x and j == y:
				continue
			if rows[j][i] == '#':
				ret += 1
	return ret


rows = [x for x in open("input", 'r').read().split("\n")]
print(isinstance(rows[0], list))


newsetup = list()
while True:
	print("starting loop")
	start = 0
	changes = 0
	newsetup = list()
	for y in range(len(rows)):
		newsetup.append(list())
		# print(row)
		for x in range(len(rows[y])):
			# print("seat nb {}({}) has {} adjacencies".format(x, rows[y][x], nbadjacencies()))
			if rows[y][x] == 'L' and nbadjacencies() == 0:
				newsetup[y].append('#')
				changes += 1
			elif rows[y][x] == '#' and nbadjacencies() >= 4:
				newsetup[y].append('L')
				changes += 1
			else:
				newsetup[y].append(rows[y][x])
	if changes == 0:
		break
	rows = newsetup

counter = 0
for row in newsetup:
	for seat in row:
		if seat == '#':
			counter += 1
	print(row, counter)
print(counter)
