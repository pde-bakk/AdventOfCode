from itertools import permutations


def parse_names(lines: list):
	for line in lines:
		words = line.split()
		person_a, happiness_units, person_b = words[0], int(words[3]), words[-1].strip('.')
		names.update([person_a, person_b])
		if person_a not in happinesses:
			happinesses[person_a] = dict()
		if words[2] == 'lose':
			happiness_units *= -1
		happinesses[person_a][person_b] = happiness_units


def permute() -> int:
	options = [list(x) for x in permutations(names)]
	total_happ, best_option = 0, None
	for option in options:
		if option[0] != 'Bob':  # Chair position does not matter, only their order
			continue
		table_happ, table_change = 0, 0
		for idx, person in enumerate(option):
			left_change = happinesses[person][option[idx - 1]]
			if idx == len(option) - 1:
				idx = -1
			right_change = happinesses[person][option[idx + 1]]
			table_happ += left_change + right_change
		if table_happ > total_happ:
			total_happ, best_option = table_happ, option
	print(f'{total_happ}, {best_option}')
	return total_happ


def part2():
	happinesses["Peer"] = dict()
	for name in names:
		happinesses["Peer"][name] = 0
		happinesses[name]["Peer"] = 0
	names.add("Peer")


names = set()
happinesses = dict()
parse_names(open('input.txt', 'r').readlines())
part2()
print(names)
print(happinesses)
print(permute())
