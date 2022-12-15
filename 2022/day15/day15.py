import re


def get_distance(a, b) -> int:
	return abs(a[0] - b[0]) + abs(a[1] - b[1])


def print_map():
	for _y in range(-2, 23):
		s = []
		for _x in range(-4, 26):
			s.append(kaart.get((_y, _x), '.'))
		print(_y, ''.join(s))


with open('input.txt', 'r') as f:
	lines = f.read().splitlines()
kaart = {}
sensors = {}
part_1 = 0

for line in lines:
	ints = list(map(int, re.findall(r'\d+', line)))
	x1, y1, x2, y2 = ints
	sensor, beacon = (y1, x1), (y2, x2)
	kaart[(y1, x1)] = 'S'
	kaart[(y2, x2)] = 'B'
	sensors[sensor] = beacon

for sensor, beacon in sorted(sensors.items()):
	y = 2000000
	distance = get_distance(sensor, beacon)
	dist_to_line = abs(sensor[0] - y)
	start = sensor[1] - (distance - dist_to_line)
	end = sensor[1] + (distance - dist_to_line)
	for x in range(start, end):
		if (y, x) not in kaart:
			kaart[(y, x)] = '#'
			part_1 += 1

print(f'Part 1: {part_1}')
