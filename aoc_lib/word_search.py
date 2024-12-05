from aoc_lib.directions import *


def word_search(lines: list[str], word_to_find: str) -> int:
	found = 0
	for y, line in enumerate(lines):
		for x, c in enumerate(line):
			for d in [EAST, SOUTH, WEST, NORTH, SOUTHWEST, SOUTHEAST, NORTHEAST, NORTHWEST]:
				p = Position(y, x)
				w = c
				for _ in range(len(word_to_find) - 1):
					p += d
					if not p.isvalid(len(lines), len(lines[0])):
						break
					w += lines[p.y][p.x]
				if w == word_to_find:
					found += 1
	return found


def diag(lines: list[str], p: Position, da: Position, db: Position) -> str:
	pa = p + da
	pb = p + db
	if not pa.isvalid(len(lines), len(lines[0])) or not pb.isvalid(len(lines), len(lines[0])):
		return ''
	return lines[pa.y][pa.x] + lines[p.y][p.x] + lines[pb.y][pb.x]


def word_search_diagonal_x(lines: list[str], word_to_find: str) -> int:
	found = 0
	for y, line in enumerate(lines):
		for x, c in enumerate(line):
			p = Position(y, x)
			a = diag(lines, p, SOUTHWEST, NORTHEAST)
			b = diag(lines, p, SOUTHEAST, NORTHWEST)
			if all(s in [word_to_find, reversed(word_to_find)] for s in [a, b]):
				found += 1
	return found
