def get_fuel(dist: int, part) -> int:
	fuel = dist // 3 - 2
	if fuel > 0 and part == 2:
		fuel += max(get_fuel(fuel, part), 0)
	return fuel


lines = [int(x) for x in open("input.txt").read().splitlines()]
print(f'part1: {sum([get_fuel(x, part=1) for x in lines])}')
print(f'part2: {sum([get_fuel(x, part=2) for x in lines])}')
