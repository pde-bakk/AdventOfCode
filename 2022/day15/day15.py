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

for line in lines:
	ints = list(map(int, re.findall(r'\d+', line)))
	x1, y1, x2, y2 = ints
	sensor, beacon = (y1, x1), (y2, x2)
	print(f'Sensor at {y1, x1}, Beacon at {y2, x2}')
	kaart[(y1, x1)] = 'S'
	kaart[(y2, x2)] = 'B'
	dist = get_distance(sensor, beacon)
	for dy in range(-dist, dist + 1):
		for dx in range(-dist, dist + 1):
			pos = (sensor[0] + dy, sensor[1] + dx)
			if pos not in kaart and abs(dx) + abs(dy) <= dist:
				kaart[pos] = '#'

# print_map()
print(f'Part 1:', sum(1 for y, x in kaart.keys() if y == 10 and kaart[(y, x)] == '#'))
