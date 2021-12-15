# from collections import deque
import heapq


def dist(grid, y: int, x: int) -> int:
	return abs(len(grid) - y) + abs(len(grid[0]) - x)


def get_tuple(grid: list[list[int]], y: int, x: int, curr_risk: int) -> tuple:
	# (g+h, h, g, y, x)
	distance = dist(grid, y, x)
	return curr_risk + distance, distance, curr_risk, y, x


def astar(grid: list[list[int]]):
	neighbours = [(-1, 0), (1, 0), (0, -1), (0, 1)]
	open_queue = []
	closed_queue = {}
	heapq.heappush(open_queue, get_tuple(grid=grid, y=0, x=0, curr_risk=0))
	solutions = []
	while open_queue:
		heur, distance, risk, y, x = heapq.heappop(open_queue)
		for neigh in neighbours:
			newy, newx = y + neigh[0], x + neigh[1]
			if newy in [-1, size] or newx in [-1, size]:
				continue
			newrisk = risk + grid[newy][newx]
			if newy == size - 1 and newx == size - 1:
				solutions.append(newrisk)
			if (newy, newx) in closed_queue.keys() and closed_queue[(newy, newx)] <= newrisk:
				continue
			heapq.heappush(open_queue, get_tuple(grid=grid, y=newy, x=newx, curr_risk=newrisk))
		if not (y, x) in closed_queue.keys() or closed_queue[(y, x)] > risk:
			closed_queue[(y, x)] = risk
	return min(solutions)


rows = [[int(x) for x in row] for row in open('input.txt').read().splitlines()]
size = len(rows)
# print(f'Part1: {astar(rows)}')
newgrid = [[0 for _ in range(5 * len(rows[0]))] for _ in range(5 * len(rows))]

for g_d in range(5):
	dpos = (g_d * size, g_d * size)
	for g_i in range(5 - g_d):
		for side in range(2):  # one time for moving horizontally, once for diagonally
			if side == 0:
				startpos = (dpos[0] + g_i * size, dpos[1])
			else:
				startpos = (dpos[0], dpos[1] + g_i * size)
			for g_y, g_row in enumerate(rows):
				for g_x, g_item in enumerate(g_row):
					newgrid[startpos[0] + g_y][startpos[1] + g_x] = g_item + g_i + 2 * g_d
					if newgrid[startpos[0] + g_y][startpos[1] + g_x] > 9:
						newgrid[startpos[0] + g_y][startpos[1] + g_x] -= 9

size = len(newgrid)

print(f'Part2: {astar(newgrid)}')
