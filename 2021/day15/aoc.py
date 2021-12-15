# from collections import deque
import heapq


def dist(grid, y: int, x: int) -> int:
	return abs(len(grid) - y) + abs(len(grid[0]) - x)


def astar(grid: list[list[int]]):
	neighbours = [(-1, 0), (1, 0), (0, -1), (0, 1)]
	open_queue = []
	closed_queue = {}
	heapq.heappush(open_queue, (0 + dist(grid, 0, 0), 0, 0, 0))  # risk, x, y
	solutions = [90000]
	while open_queue:
		heur, risk, y, x = heapq.heappop(open_queue)
		# print(f'heur={heur},risk={risk},y={y}, x={x}')
		for neigh in neighbours:
			newy = y + neigh[0]
			newx = x + neigh[1]
			if newy in [-1, len(grid)] or newx in [-1, len(grid)]:
				continue
			newrisk = risk + grid[newy][newx]
			if newy == len(grid) - 1 and newx == len(grid[0]) - 1:
				# print(f'found way to exit with risk {newrisk}')
				solutions.append(newrisk)
			if (newy, newx) in closed_queue.keys() and closed_queue[(newy, newx)] <= newrisk:
				continue
			# print(f'grid[{newy}][{newx}]={grid[newy][newx]}, totalrisk={newrisk}')
			heapq.heappush(open_queue, (newrisk + dist(grid, newy, newx), newrisk, newy, newx))
		if not (y, x) in closed_queue.keys() or closed_queue[(y, x)] > risk:
			closed_queue[(y, x)] = risk
	return min(solutions)


rows = [[int(x) for x in row] for row in open('input.txt').read().splitlines()]
newgrid = [[0 for _ in range(5 * len(rows[0]))] for _ in range(5 * len(rows))]

for d in range(1):
	startpos = (d * len(rows), d * len(rows[0]))
	for i in range(5):
		for side in range(2):  # one time for moving horizontally, once for diagonally
			if side == 0:
				startpos += (i * len(rows), 0)
			else:
				startpos += (0, i * len(rows[0]))
			for y, row in enumerate(rows):
				for x, item in enumerate(row):
					newgrid[startpos[0] + y][startpos[1] + x] = item + i
					if newgrid[startpos[0] + y][startpos[1] + x] > 9:
						newgrid[startpos[0] + y][startpos[1] + x] -= 9

for row in newgrid:
	print(row)
# print(f'Part1: {astar(rows)}')
