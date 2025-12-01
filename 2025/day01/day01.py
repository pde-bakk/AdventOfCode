import sys
from typing import Tuple

import math

sys.path.append('../..')
from aoc_lib.get_input import get_input_file, get_example_file
from aoc_lib.utilities import *
from aoc_lib.extra_input_utils import *
from aoc_lib.directions import *


def parse(data: str) -> list[str]:
    lines = split_data_on_newlines(data)
    return lines


def solve(lines: list[str]) -> Tuple[int, int]:
    dial = 50
    part1 = part2 = 0
    for line in lines:
       direction = line[0]
       amount = int(line[1:])
       if direction == 'L':
          zeroes = (dial - 1) // 100 - (dial - amount - 1) // 100
          dial -= amount
       elif direction == 'R':
          zeroes = (dial + amount) // 100
          dial += amount
       else:
          raise Exception(f'Invalid direction: {direction}')
       part2 += zeroes
       dial %= 100
       if dial == 0:
          part1 += 1
    return part1, part2


def aoc(data: str, args, prefix: str) -> None:
    lines = parse(data)
    part1, part2 = solve(lines)
    print(f'{prefix}: Part 1: {part1}, part 2: {part2}')


if __name__ == '__main__':
    program_args = parse_args()
    if 'example' in program_args.mode:
       aoc(get_example_file(), program_args, 'Example')
    if 'solution' in program_args.mode:
       aoc(get_input_file(), program_args, 'Solution')
