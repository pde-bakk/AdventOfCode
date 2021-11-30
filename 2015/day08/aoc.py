from typing import List


def part1(rows: List[str]) -> int:
	ret = 0
	for row in rows:
		if row:
			ret += len(row) - len(eval(row))
	return ret


def part2(rows: List[str]) -> int:
	ret = 0
	for row in rows:
		if row:
			encoded_len = len(row) + 2 + row.count("\"") + row.count("\\")
			ret += encoded_len - len(row)
	return ret


lines = open('input.txt', 'r').read().split('\n')
print(part1(lines))
print(part2(lines))
