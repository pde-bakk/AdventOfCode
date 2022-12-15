import re


def get_distance(a, b) -> int:
	return abs(a[0] - b[0]) + abs(a[1] - b[1])


with open('input.txt', 'r') as f:
	lines = f.read().splitlines()
kaart = set()
sensors = {}

for line in lines:
	x1, y1, x2, y2 = map(int, re.findall(r'-?\d+', line))
	sensor, beacon = (y1, x1), (y2, x2)
	sensors[sensor] = beacon

for sensor, beacon in sensors.items():
	y = 2000000
	distance = get_distance(sensor, beacon)
	dist_to_line = abs(sensor[0] - y)
	start = sensor[1] - (distance - dist_to_line)
	end = sensor[1] + (distance - dist_to_line)
	for x in range(start, end):
		kaart.add(x)

print(f'Part 1: {len(kaart)}')
