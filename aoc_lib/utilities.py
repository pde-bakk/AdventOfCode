import re


def lmap(func, *it) -> list:
	return list(map(func, *it))


def ints(s: str) -> list[int]:
	return lmap(int, re.findall(r'-?\d+', s))


def pos_ints_only(s: str) -> list[int]:
	return lmap(int, re.findall(r'\d+', s))


def floats(s: str) -> list[float]:
	return lmap(float, re.findall(r'-?\d+(?:\.\d+)?', s))


def positive_floats(s: str) -> list[float]:
	return lmap(float, re.findall(r'\d+(?:\.\d+)?', s))


def words(s: str) -> list[str]:
	return re.findall(r'[a-zA-Z]+', s)


def get_directions(diagonal: bool = False) -> list[tuple[int, int]]:
	directions = [
		(0, 1),  # South
		(0, -1),  # North
		(1, 0),  # East
		(-1, 0),  # West
	]
	if diagonal:
		directions += [
			(1, 1),  # South East
			(1, -1),  # South West
			(-1, 1),  # North East
			(-1, -1)  # North West
		]
	return directions


def yield_directions(diagonal: bool = False) -> tuple[int, int]:
	for direction in get_directions(diagonal=diagonal):
		yield direction


def get_neighbours(y: int, x: int, diagonal: bool = False) -> list[tuple[int, int]]:
	return [(y + d[0], x + d[1]) for d in get_directions(diagonal=diagonal)]


def yield_neighbours(y: int, x: int, diagonal: bool = False) -> tuple[int, int]:
	for n in get_neighbours(y, x, diagonal):
		yield n


def distance(pos1: tuple[int, int], pos2: tuple[int, int]) -> float:
	return ((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2) ** 0.5


def manhattan_distance(pos1: tuple[int, int], pos2: tuple[int, int]) -> int:
	return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])


def replace_all(s: str, chars_to_replace: str, replacement: str = '') -> str:
	for c in chars_to_replace:
		s = s.replace(c, replacement)
	return s
