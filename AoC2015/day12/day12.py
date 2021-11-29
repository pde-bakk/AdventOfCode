import json


def recurse(whatever) -> int:
	total = 0
	if isinstance(whatever, list):
		for item in whatever:
			total += recurse(item)
	elif isinstance(whatever, dict):
		for item in whatever:
			total += recurse(whatever[item])
	elif isinstance(whatever, int):
		total += whatever
	return total


def part1(filename: str) -> int:
	js = json.load(open(filename, 'r'))
	return sum([recurse(item) for item in js])


print(f'the answer is {part1("input.txt")}')
