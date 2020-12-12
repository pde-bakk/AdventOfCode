# import math

rows = [x for x in open("input.txt", 'r').read().split("\n")]
waypointx, waypointy = 10, 1
shipx, shipy = 0, 0
up, side = 0, 0
turn = 0

for row in rows:
	direction = row[0]
	value = int(row[1:])
	# print("direction={}, value = {}".format(direction, value))
	if direction == 'E':
		waypointx += value
	elif direction == 'W':
		waypointx -= value
	elif direction == 'N':
		waypointy += value
	elif direction == 'S':
		waypointy -= value
	elif direction in ('L', 'R'):
		print("at start, waypoint is at {}, {}".format(waypointx, waypointy))
		if value == 180:
			waypointx, waypointy = -waypointx, -waypointy
		elif (direction == 'L' and value == 90) or (direction == 'R' and value == 270):
			waypointx, waypointy = -waypointy, waypointx
		elif (direction == 'L' and value == 270) or (direction == 'R' and value == 90):
			waypointx, waypointy = waypointy, -waypointx
		print("at the end, waypoint is at {}, {}".format(waypointx, waypointy))
	elif direction == 'F':
		shipx += value * waypointx
		shipy += value * waypointy

print(abs(shipx)+abs(shipy))
