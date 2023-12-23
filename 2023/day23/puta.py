import sys
import math

sys.path.append('../..')
from aoc_lib.get_input import get_input_file, get_example_file
from aoc_lib.utilities import *
from aoc_lib.extra_input_utils import *
from aoc_lib.directions import *


with open('input.txt', 'r') as f:
    data = f.read().strip().splitlines()


# Part 1
edges = {}
for r, row in enumerate(data):
    for c, v in enumerate(row):
        if v == ".":
            for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                ar, ac = r + dr, c + dc
                if not (0 <= ar < len(data) and 0 <= ac < len(row)):
                    continue
                if data[ar][ac] == ".":
                    edges.setdefault((r, c), set()).add((ar, ac))
                    edges.setdefault((ar, ac), set()).add((r, c))
        if v == ">":
            edges.setdefault((r, c), set()).add((r, c + 1))
            edges.setdefault((r, c - 1), set()).add((r, c))
        if v == "v":
            edges.setdefault((r, c), set()).add((r + 1, c))
            edges.setdefault((r - 1, c), set()).add((r, c))

n, m = len(data), len(data[0])

q = [(0, 1, 0)]
visited = set()
best = 0
while q:
    r, c, d = q.pop()
    if d == -1:
        visited.remove((r, c))
        continue
    if (r, c) == (n - 1, m - 2):
        best = max(best, d)
        continue
    if (r, c) in visited:
        continue
    visited.add((r, c))
    q.append((r, c, -1))
    for ar, ac in edges[(r, c)]:
        q.append((ar, ac, d + 1))
print(best)

# Part 2
edges = {}  # (r, c) -> (ar, ac, length)
for r, row in enumerate(data):
    for c, v in enumerate(row):
        if v in ".>v":
            for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                ar, ac = r + dr, c + dc
                if not (0 <= ar < len(data) and 0 <= ac < len(row)):
                    continue
                if data[ar][ac] in ".>v":
                    edges.setdefault((r, c), set()).add((ar, ac, 1))
                    edges.setdefault((ar, ac), set()).add((r, c, 1))

# Remove nodes with degree 2 by merging the edges
while True:
    for n, e in edges.items():
        if len(e) == 2:
            a, b = e
            print(f'{a=}, {b=}, {a[:2]=}, {n + (a[2],)=}')
            edges[a[:2]].remove(n + (a[2],))
            edges[b[:2]].remove(n + (b[2],))
            edges[a[:2]].add((b[0], b[1], a[2] + b[2]))
            edges[b[:2]].add((a[0], a[1], a[2] + b[2]))
            del edges[n]
            break
    else:
        break
print(edges[(0, 1)])
exit()
n, m = len(data), len(data[0])

q = [(0, 1, 0)]
visited = set()
best = 0
while q:
    r, c, d = q.pop()
    if d == -1:
        visited.remove((r, c))
        continue
    if (r, c) == (n - 1, m - 2):
        best = max(best, d)
        continue
    if (r, c) in visited:
        continue
    visited.add((r, c))
    q.append((r, c, -1))
    for ar, ac, l in edges[(r, c)]:
        q.append((ar, ac, d + l))
print(best)
