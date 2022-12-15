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

for line in lines:
	ints = list(map(int, re.findall(r'\d+', line)))
	x1, y1, x2, y2 = ints
	sensor, beacon = (y1, x1), (y2, x2)
	print(f'Sensor at {y1, x1}, Beacon at {y2, x2}')
	kaart[(y1, x1)] = 'S'
	kaart[(y2, x2)] = 'B'
	sensors[sensor] = beacon

y = 2_000_000
part_1 = 0
for x in range(-10_000_000, 10_000_000):
	possible = True
	if x % 100_000 == 0:
		print(x)
	for sensor, beacon in sensors.items():
		if (y, x) == beacon:
			possible = False
			break
		if get_distance(sensor, (x, y)) <= get_distance(sensor, beacon):
			possible = False
			break
	if not possible:
		part_1 += 1

print(f'Part 1: {part_1}')
