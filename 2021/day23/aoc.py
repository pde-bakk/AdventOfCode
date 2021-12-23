import copy
import heapq
import operator
import math
from collections import deque

tiebreaker = 0
best = math.inf


def get_neighbours():
	for n in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
		yield n


class Node:
	grid = []
	#          y, x ,  y, x
	goal_a = ((2, 3), (3, 3))
	goal_b = ((2, 5), (3, 5))
	goal_c = ((2, 7), (3, 7))
	goal_d = ((2, 9), (3, 9))
	goals = [goal_a, goal_b, goal_c, goal_d]

	def __init__(self, arg=None):
		if arg is None:
			self.a = []
			self.b = []
			self.c = []
			self.d = []
			self.g = 0
			self.h = 0
			self.energy = 0
		elif isinstance(arg, Node):
			self.a = arg.a.copy()
			self.b = arg.b.copy()
			self.c = arg.c.copy()
			self.d = arg.d.copy()
			self.g = arg.g
			self.h = arg.h
			self.energy = arg.energy
		global tiebreaker
		self.tiebreaker = tiebreaker
		tiebreaker += 1

	def gethash(self):
		return tuple(sorted(self.a)) + tuple(sorted(self.b)) + tuple(sorted(self.c)) + tuple(sorted(self.d))

	def __lt__(self, other):
		selff = self.f()
		otherf = other.f()
		if selff != otherf:
			return selff < otherf
		if self.h != other.h:
			return self.h < other.h
		if self.g != other.g:
			return self.g < other.g
		return self.tiebreaker < other.tiebreaker

	def __iter__(self):
		for amphipod in [self.a, self.b, self.c, self.d]:
			yield amphipod

	def __getitem__(self, item: int) -> list[tuple[int, int], tuple[int, int]]:
		if item < -1 or item >= 4:
			raise IndexError
		return [self.a, self.b, self.c, self.d][item]

	def get_amphipods(self):
		for pos, goal in zip(self.__iter__(), [Node.goal_a, Node.goal_b, Node.goal_c, Node.goal_d]):
			yield pos, goal

	def heuristic(self):
		self.h = 0
		for pos, goal in self.get_amphipods():
			first = tuple(map(operator.sub, pos[0], goal[0]))
			second = tuple(map(operator.sub, pos[1], goal[1]))
			dist = abs(first[0]) + abs(first[1]) + abs(second[0]) + abs(second[1])
			# print(f'dist={dist}')
			self.h += dist
		return self.h

	def f(self) -> int:
		return self.g + self.h

	@staticmethod
	def replace_amphipods():
		start = Node()
		for y, row in enumerate(Node.grid):
			for x, space in enumerate(row):
				if space in ['A', 'B', 'C', 'D']:
					match space:
						case 'A':
							start.a.append((y, x))
						case 'B':
							start.b.append((y, x))
						case 'C':
							start.c.append((y, x))
						case 'D':
							start.d.append((y, x))
					Node.grid[y][x] = ' '
		start.heuristic()
		return start

	def __repr__(self) -> str:
		s = str()
		for y, row in enumerate(self.grid):
			for x, item in enumerate(row):
				if (y, x) in self.a:
					s += 'A'
				elif (y, x) in self.b:
					s += 'B'
				elif (y, x) in self.c:
					s += 'C'
				elif (y, x) in self.d:
					s += 'D'
				else:
					s += item
			s += '\n'
		s += f'F={self.g + self.h}\n'
		s += f'Energycost: {self.g}\n'
		s += f'Heuristic: {self.h}\n'
		return s

	def move_is_possible(self, movetile) -> bool:
		if any(c == -1 for c in movetile):
			return False
		my, mx = movetile
		if Node.grid[my][mx] == '#':
			return False
		if any(movetile in x for x in [self.a, self.b, self.c, self.d]):
			return False
		return True

	def perform_moves(self, closed_queue: dict = None):
		for i, amphipods in enumerate(self.__iter__()):
			for amphi_idx, amphi in enumerate(amphipods):
				for n in get_neighbours():
					ay, ax = amphi
					# print(f'{amphi} in {Node.goals[i]}i={i}: {amphi in Node.goals[i]}')
					# print(f'tile below is Node.grid[{ay + 1}][{ax}] = {Node.grid[ay-1][ax]}')
					if amphi in Node.goals[i] and (Node.grid[ay + 1][ax] == '#' or amphipods[amphi_idx - 1] == (amphi[0] + 1, amphi[1])):
						continue
					target_pos = tuple(map(operator.add, amphi, n))
					if -1 in target_pos:
						raise IndexError  # Shouldn't happen
					if Node.grid[target_pos[0]][target_pos[1]] == '#':
						continue  # Blocked by a wall
					if any(target_pos in x for x in self.__iter__()):
						continue  # Blocked by another amphipod
					new_node = Node(self)
					listy = new_node[i]
					listy[amphi_idx] = target_pos
					new_node.g += 1
					new_node.energy += 10 ** i
					new_node.heuristic()
					# if new_node.gethash() not in closed_queue.keys():
					# 	# print(f'i, amphipods = {i}, {amphipods}')
					# 	# print(f'amphi_idx, amphi = {amphi_idx}, {amphi}')
					# 	# print(f'n, target_pos = {n}, {target_pos}')
					# 	print(f'new_node = \n{new_node}')
					yield new_node


def pathfind(start: Node) -> int:
	print(f'LETS START PATHFINDING')
	closed_queue = {}
	open_queue = []
	heapq.heappush(open_queue, start)
	i = 0
	while len(open_queue) > 0:
		node = heapq.heappop(open_queue)
		print(f'POPPING node:\n{node}')
		if node.h < 1:
			print(f'h={node.h}')
			print(node)
			return node.g
		for move in node.perform_moves(closed_queue):
			hashy = move.gethash()
			if hashy in closed_queue.keys() and closed_queue[hashy] <= move.g:
				continue
			heapq.heappush(open_queue, move)
		hashy = node.gethash()
		if hashy not in closed_queue.keys() or closed_queue[hashy] > node.g:
			# print(f'adding node to closed_queue')
			closed_queue[node.gethash()] = node.g
		# print(f'len open_queue is {len(open_queue)}')
		if i == 3:
			break
		# i += 1
	print(f'open_queue still has a length of {len(open_queue)}')
	print(f'closed queue has {len(closed_queue)} items in it')
	return 0


def bfs(start: Node) -> int:
	print(f'LETS START PATHFINDING')
	open_queue = deque()
	open_queue.append(start)
	i = 0
	while len(open_queue) > 0:
		node = open_queue.popleft()
		# print(f'POPPING node:\n{node}')
		if node.h < 1:
			print(f'h={node.h}')
			print(node)
			return node.g
		for move in node.perform_moves():
			# hashy = move.gethash()
			# if hashy in closed_queue.keys() and closed_queue[hashy] <= move.g:
			# 	continue
			open_queue.append(move)
			# heapq.heappush(open_queue, move)
		# hashy = node.gethash()
		# if hashy not in closed_queue.keys() or closed_queue[hashy] > node.g:
		# 	# print(f'adding node to closed_queue')
		# 	closed_queue[node.gethash()] = node.g
		# print(f'len open_queue is {len(open_queue)}')
		if i == 3:
			break
		# i += 1
	print(f'open_queue still has a length of {len(open_queue)}')
	# print(f'closed queue has {len(closed_queue)} items in it')
	return 0


def parse(fstr: str) -> Node:
	with open(fstr, 'r') as f:
		rows = f.read().splitlines()
		grid = [[c for c in r] for r in rows]
	Node.grid = copy.deepcopy(grid)
	return Node.replace_amphipods()


def main(fstr: str):
	start = parse(fstr)
	print(start)
	# ans = pathfind(start)
	ans = bfs(start)
	print(f'ans={ans}')
	return ans


if __name__ == '__main__':
	ret = main('example.txt')
