def movesanta(x, y):
	if c == '^': y += 1
	elif c == 'v': y -= 1
	elif c == '>': x += 1
	elif c == '<': x -= 1
	houses.add((x, y))
	return x, y


sx, sy = 0, 0
rx, ry = 0, 0
houses = {(sx, sy)}
for i, c in enumerate(open('input', 'r').read()):
	if i % 2 == 0:
		sx, sy = movesanta(sx, sy)
	else:
		rx, ry = movesanta(rx, ry)
print(len(houses))