import heapq
import copy
from collections import deque, defaultdict


class Node:
	def __init__(self, pos: list):
		self.y, self.x = pos
		self.visited = set()
		self.visited.add(tuple(pos))

	def dist_to_goal(self) -> int:
		return abs(self.y - goal.y) + abs(self.x - goal.x)

	def __lt__(self, other):
		# return self.dist_to_goal() + len(self.visited) < other.dist_to_goal() + len(other.visited)
		return len(self.visited) < len(other.visited)

	# def __iadd__(self, other):
	# 	if not isinstance(other, Node):
	# 		return NotImplemented
	# 	self.y += other.y
	# 	self.x += other.x
	# 	return self

	def __add__(self, other):
		if not isinstance(other, Node):
			return NotImplemented
		out = copy.deepcopy(self)
		out.y += other.y
		out.x += other.x
		# if (out.y, out.x) in out.visited:
		# 	out.x, out.y = -1, -1
		out.visited.add((out.y, out.x))
		return out

	def isvalid(self) -> bool:
		return 0 <= self.x < len(lines[0]) and 0 <= self.y < len(lines)


def set_start_and_goal(rows: list[str]):
	s, g = None, None
	for y, row in enumerate(rows):
		for x, alpha in enumerate(row):
			if alpha == 'S':
				s = Node([y, x])
				lines[y] = lines[y].replace('S', 'a')
			elif alpha == 'E':
				g = Node([y, x])
				lines[y] = lines[y].replace('E', 'z')
	return s, g


with open('input.txt', 'r') as f:
	lines = f.read().splitlines()
start, goal = set_start_and_goal(lines)

lines = [[ord(c) for c in line] for line in lines]
neighbours = [Node([yy, xx]) for yy, xx in [(1, 0), (0, 1), (0, -1), (-1, 0)]]

assert start and goal
print(f'start = {start.y, start.x}, goal = {goal.y, goal.x}')
# Q = [start]
Q = deque([start])
kaart = [['.' for _ in line]for line in lines]
found = False
visited = set()
visited.add((start.y, start.x))


while Q and not found:
	node = Q.popleft()
	height = lines[node.y][node.x]
	for n in neighbours:
		new_node = node + n
		k = new_node.y, new_node.x
		if k not in visited and new_node.isvalid():
			new_height = lines[new_node.y][new_node.x]
			if new_height - 1 <= height:
				visited.add(k)
				if new_height == ord('z'):
					print(f'Part 1: {len(node.visited)}')
					found = True
					for loc in node.visited:
						kaart[loc[0]][loc[1]] = '#'
					kaart[start.y][start.x] = 'S'
					kaart[goal.y][goal.x] = 'E'
					break
				Q.append(new_node)
for row in kaart:
	print(''.join(row))
