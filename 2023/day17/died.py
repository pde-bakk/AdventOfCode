import heapq
import sys
import math

sys.path.append('../..')
from aoc_lib.get_input import get_input_file, get_example_file
from aoc_lib.utilities import *
from aoc_lib.extra_input_utils import *
from aoc_lib.directions import *


from heapq import heapify, heappop, heappush

def find_end(a, b, c):
    best = {}
    heapify(queue := [(0, 1, 0, (0, 0))])
    while queue:
        loss, chain, direction, current = heappop(queue)
        if (key := (current, direction, chain)) in best and best[key] <= loss:
            continue
        if current == end and chain >= a:
            return loss
        best[key] = loss
        neighbours = adj(*current)
        for e, d in enumerate([(direction - 1) % 4, direction, (direction + 1) % 4]):
            if [chain < b, chain == c][e % 2]:
                continue
            next_chain = [1, chain + 1][e % 2]
            if (neighbour := neighbours[d]) in grid and best.get((neighbour, d, next_chain), loss + 1) > loss:
                heappush(queue, (loss + grid[neighbour], next_chain, d, neighbour))


with open("input.txt", "r") as file:
    data = file.read().splitlines()
    grid = {(x, y) : int(data[y][x]) for x in range(len(data[0])) for y in range(len(data))}
    end = (len(data[0]) - 1, len(data) - 1)
    adj = lambda x, y: ((x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1))
    print(find_end(0, 0, 3), find_end(4, 4, 10))
