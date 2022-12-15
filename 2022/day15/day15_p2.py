import re
import z3


def get_distance(a, b) -> int:
	return abs(a[0] - b[0]) + abs(a[1] - b[1])


with open('input.txt', 'r') as f:
	lines = f.read().splitlines()
sensors = {}
pairings = (
	(0, 1, 2, 3),
	(0, 2, 1, 3),
	(0, 3, 1, 2)
)

for line in lines:
	x1, y1, x2, y2 = map(int, re.findall(r'-?\d+', line))
	sensor, beacon = (y1, x1), (y2, x2)
	sensors[sensor] = get_distance(sensor, beacon)

solver = z3.Solver()
x, y = z3.Int('x'), z3.Int('y')
solver.add(x >= 0, x <= 4_000_000)
solver.add(y >= 0, y <= 4_000_000)

for sensor, distance in sensors.items():
	solver.add(z3.Abs(sensor[0] - y) + z3.Abs(sensor[1] - x) > distance)
solver.check()
model = solver.model()
print('Part 2:', model[x].as_long() * 4_000_000 + model[y].as_long())
