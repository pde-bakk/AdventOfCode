import sys
import math
import typing
import functools

sys.path.append('../..')
from aoc_lib.get_input import get_input_file, get_example_file
from aoc_lib.utilities import *
from aoc_lib.extra_input_utils import *


@functools.lru_cache
def check_legality(s: str, nbs: tuple[int, ...]) -> int:
	if not s:
		return int(len(nbs) == 0)
	elif len(nbs) == 0:
		# return int('#' not in s and '?' not in s)
		return int('#' not in s)

	if s.startswith('#'):
		first_nb, *rest = nbs
		if '.' in s[:first_nb] or len(s) < first_nb:
			return 0  # Can't fit all the necessary springs
		elif len(s) == first_nb:
			# print(f'{len(s)}=={first_nb}')
			return int(len(nbs) == 1)  # One spring, correct size
		elif s[first_nb] == '#':
			# print(f'{s}, s[{first_nb}] = #')
			return 0  # Too many consecutive #'s
		else:
			s = s[first_nb+1:].strip('.')
			return check_legality(s, nbs[1:])

	s1 = ('#' + s[1:]).strip('.')
	s2 = ('.' + s[1:]).strip('.')
	return check_legality(s1, nbs) + check_legality(s2, nbs)


def aoc(data: str, prefix: str) -> None:
	lines = split_data_on_newlines(data)
	part1 = 0
	part2 = 0
	for s, nbs in map(str.split, lines):
		nbs = tuple(int(d) for d in nbs.split(','))
		s2 = '?'.join(s for _ in range(5))
		nbs2 = tuple(nbs * 5)
		part1 += check_legality(s.strip('.'), nbs)
		part2 += check_legality(s2.strip('.'), nbs2)
	print(f'{prefix} part 1: {part1}')
	print(f'{prefix} part 2: {part2}')


if __name__ == '__main__':
	aoc(get_example_file(), 'Example')
	aoc(get_input_file(), 'Solution')
