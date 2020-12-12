rows = [x for x in open("input.txt", 'r').read().split("\n")]
up, side = 0, 0
turn = 0

for row in rows:
	direction = row[0]
	value = int(row[1:])
	print("dir = {}. value = {}".format(direction, value))
	if direction == 'F':
		rem = turn % 360
		print("turn = ", turn, "rem = ", rem)
		if rem == 0:
			direction = 'E'
			print("Forward means East")
		elif rem == 90:
			direction = 'S'
			print("Forward means South")
		elif rem == 180:
			direction = 'W'
			print("Forward means West")
		elif rem == 270:
			direction = 'N'
			print("Forward means North")

	if direction == 'E':
		side += value
	elif direction == 'W':
		side -= value
	elif direction == 'N':
		up += value
	elif direction == 'S':
		up -= value
	elif direction == 'L':
		turn += 3 * value
	elif direction == 'R':
		turn += value

	print("north={}, east={}, sum={}".format(up, side, abs(up) + abs(side)))
print("north={}, east={}, sum={}".format(up, side, abs(up) + abs(side)))