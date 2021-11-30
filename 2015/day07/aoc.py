from typing import List

results = {}


def get_value(key: str):
	try:
		return int(key)
	except ValueError:
		pass
	cmd = key.split()
	if len(cmd) == 1:
		# print(f'key = {key}, results[key] = {results[key]}')
		results[key] = get_value(results[key])
		return get_value(results[key])
	if cmd[0] == 'NOT':
		return ~get_value(cmd[1])
	if cmd[1] == 'AND':
		return get_value(cmd[0]) & get_value(cmd[2])
	if cmd[1] == 'OR':
		return get_value(cmd[0]) | get_value(cmd[2])
	if cmd[1] == 'LSHIFT':
		return get_value(cmd[0]) << get_value(cmd[2])
	if cmd[1] == 'RSHIFT':
		return get_value(cmd[0]) >> get_value(cmd[2])


def part1(lines: List[str]) -> int:
	results.clear()
	for line in lines:
		if not line:
			break
		command, result = line.split(' -> ')
		results[result] = command
	return get_value('a')


def part2(lines: List[str], ) -> int:
	value_a = part1(lines)
	results.clear()
	for line in lines:
		if not line:
			break
		command, result = line.split(' -> ')
		results[result] = command
	results['b'] = value_a
	return get_value('a')


rows = open('input.txt', 'r').read().split('\n')
print(part1(rows))
print(results)

print(f'part 2 gives {part2(rows)}')
