import copy
import heapq
import operator
import math
from collections import deque
import time
import sys
import enum


MAX_X = MAX_Y = 0


class Cucumber(enum.IntEnum):
    EMPTY = 0
    EAST = 1
    SOUTH = 2


def parse(fstr: str):
    with open(fstr, 'r') as f:
        rows = f.read().splitlines()
    global MAX_X, MAX_Y
    MAX_X, MAX_Y = len(rows[0]), len(rows)
    print(f'max_x = {MAX_X}, max_y={MAX_Y}')
    return [row for row in rows]


def get_pos_dict(grid) -> tuple[dict[tuple, int], dict[tuple, int]]:
    easts = {}
    souths = {}
    for y, row in enumerate(grid):
        for x, item in enumerate(row):
            match item:
                case 'v':
                    souths[(y, x)] = Cucumber.SOUTH
                case '>':
                    easts[(y, x)] = Cucumber.EAST
                case _:
                    pass
    return easts, souths


def get_movetarget(pos: tuple, direction: int) -> tuple:
    # global MAX_X, MAX_Y
    match direction:
        case Cucumber.EAST:
            if pos[1] == MAX_X - 1:
                return pos[0], 0
            return tuple(map(operator.add, pos, (0, 1)))
        case Cucumber.SOUTH:
            if pos[0] == MAX_Y - 1:
                return 0, pos[1]
            return tuple(map(operator.add, pos, (1, 0)))
        case _:
            raise KeyError


def visualize(south: dict, east: dict):
    res = str()
    for y in range(MAX_Y):
        for x in range(MAX_X):
            if (y, x) in south and (y, x) in east:
                raise AssertionError
            if (y, x) in south:
                res += 'v'
            elif (y, x) in east:
                res += '>'
            else:
                res += '.'
        res += '\n'
    print(res)


def loop(grid: list[str]) -> int:
    eastbounds, southbounds = get_pos_dict(grid)
    visualize(southbounds, eastbounds)
    moves = 1
    step = 0
    while moves > 0:
        moves = 0
        new_eastbounds = {}
        for k, v in eastbounds.items():
            target = get_movetarget(k, v)
            if target in eastbounds or target in southbounds:
                new_eastbounds[k] = v
                continue
            new_eastbounds[target] = v
            moves += 1
        eastbounds = new_eastbounds

        new_southbounds = {}
        for k, v in southbounds.items():
            target = get_movetarget(k, v)
            if target in southbounds or target in eastbounds:
                new_southbounds[k] = v
                continue
            new_southbounds[target] = v
            moves += 1
        southbounds = new_southbounds
        step += 1
        # print(f'after {step} steps:')
        # visualize(southbounds, eastbounds)
        # break
    return step


def main(fstr: str, part: int = 1):
    grid = parse(fstr)
    ans = loop(grid)
    return ans


if __name__ == '__main__':
    assert main('example.txt') == 58
    print(f'Part1: {main("input.txt")}')
