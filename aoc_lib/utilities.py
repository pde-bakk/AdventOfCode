import math
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


def distance(pos1: tuple[int, int], pos2: tuple[int, int]) -> float:
	return ((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2) ** 0.5


def manhattan_distance(pos1: tuple[int, int], pos2: tuple[int, int]) -> int:
	return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])


def replace_all(s: str, chars_to_replace: str, replacement: str = '') -> str:
	for c in chars_to_replace:
		s = s.replace(c, replacement)
	return s

def concatenate_ints(a: int, b: int) -> int:
	# Could do it with int(str(a) + str(b)), but that is slow
	return a * 10 * math.ceil(math.log10(b + 1)) + b

