def nbadjacencies():
	ret = 0
	directions = (-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)
	for dx, dy in directions:
		i, j = x + dx, y + dy
		# if x == 0 and y == 1:
		# 	print("dx, dy = {}, {}\ti, j = {}, {}".format(dx, dy, i, j))
		while i in range(0, len(rows[y])) and j in range(0, len(rows)):
			if rows[j][i] == 'L':
				break
			elif rows[j][i] == '#':
				ret += 1
				# if x == 0 and y == 1:
				# 	print("{}th obstacle in direction {},{}".format(ret, dx, dy))
				break
			i += dx
			j += dy
	return ret


rows = [x for x in open("input", 'r').read().split("\n")]
print(isinstance(rows[0], list))


newsetup = list()
iterations = 0
while True:
	print("starting loop", iterations)
	start = 0
	changes = 0
	newsetup = list()
	for y in range(len(rows)):
		newsetup.append(list())
		# print(''.join(rows[y]))
		for x in range(len(rows[y])):
			# print("seat nb {}({}) has {} adjacencies".format(x, rows[y][x], nbadjacencies()))
			if rows[y][x] == 'L' and nbadjacencies() == 0:
				newsetup[y].append('#')
				changes += 1
			elif rows[y][x] == '#' and nbadjacencies() >= 5:

				newsetup[y].append('L')
				changes += 1
			else:
				newsetup[y].append(rows[y][x])
	if changes == 0: # or iterations > 5:
		break
	rows = newsetup
	iterations += 1

counter = 0
for row in newsetup:
	for seat in row:
		if seat == '#':
			counter += 1
	print(row, counter)
print(counter)
