from itertools import permutations


names = set()
happinesses = dict()


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
	total_happ, total_change, best_option = 0, 0, None
	for option in options:
		if option[0] != 'Bob':  # Chair position does not matter, only their order
			continue
		table_happ, table_change = 0, 0
		for idx, person in enumerate(option):
			left_change = happinesses[person][option[idx - 1]]
			# print(f'idx={idx}, person={person} left={option[idx - 1]} ({left_change})')
			if idx == len(option) - 1:
				idx = -1
			right_change = happinesses[person][option[idx + 1]]
			# print(f'idx={idx}, person={person} right={option[idx + 1]} ({right_change})')
			table_happ += left_change + right_change
			table_change += abs(left_change) + abs(right_change)
		print(f'{option} gives {table_happ}')
		if table_happ > total_happ:
			total_happ, total_change, best_option = table_happ, table_change, option
		# print(option)
	print(f'{total_happ}, {total_change}, {best_option}')
	return total_change


def part2():
	happinesses["Peer"] = dict()
	for name in names:
		happinesses["Peer"][name] = 0
		happinesses[name]["Peer"] = 0
	names.add("Peer")


parse_names(open('input.txt', 'r').readlines())
part2()

print(names)
print(happinesses)
print(permute())
