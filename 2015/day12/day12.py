import json


def recurse(whatever) -> int:
	total = 0
	if isinstance(whatever, list):
		for item in whatever:
			total += recurse(item)
	elif isinstance(whatever, dict) and 'red' not in whatever.values():
		for item in whatever:
			total += recurse(whatever[item])
	elif isinstance(whatever, int):
		total += whatever
	return total


js = json.load(open('input.txt', 'r'))
print(sum([recurse(item) for item in js]))
