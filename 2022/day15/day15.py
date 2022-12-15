import re


def get_distance(a, b) -> int:
	return abs(a[0] - b[0]) + abs(a[1] - b[1])


def print_map():
	for y in range(-2, 23):
		s = []
		for x in range(-4, 26):
			s.append(kaart.get((y, x), '.'))
		print(y, ''.join(s))


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

for sensor, beacon in sensors.items():
	y = 2000000
	distance = get_distance(sensor, beacon)
	print(f'Sensor at {sensor}, Beacon at {beacon}, distance = {distance}')
	for dx in range(-distance, distance + 1):
		pos = (y, sensor[1] + dx)
		if get_distance(pos, sensor) > distance:
			continue
		if pos not in kaart:
			kaart[pos] = '#'
			part_1 += 1

print(f'Part 1: {part_1}')
