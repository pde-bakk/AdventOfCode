import copy
import heapq
import operator
import math
from collections import deque
import time

tiebreaker = 0


def get_neighbours():
	for n in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
		yield n


class Node:
	grid = []
	GOAL_Y = [2, 3]
	goal_ax, goal_bx, goal_cx, goal_dx = 3, 5, 7, 9
	goal_a, goal_b, goal_c, goal_d = (), (), (), ()
	goals = [goal_a, goal_b, goal_c, goal_d]
	doors = ((1, 3), (1, 5), (1, 7), (1, 9))

	def __init__(self, arg=None):
		if arg is None:
			self.a = []
			self.b = []
			self.c = []
			self.d = []
			self.g = 0
			self.h = 0
			self.parent = None
		elif isinstance(arg, Node):
			self.a = arg.a.copy()
			self.b = arg.b.copy()
			self.c = arg.c.copy()
			self.d = arg.d.copy()
			self.g = arg.g
			self.h = arg.h
			self.parent = arg
		global tiebreaker
		self.tiebreaker = tiebreaker
		tiebreaker += 1

	@staticmethod
	def setgoals(part: int = 1):
		if part == 2:
			Node.GOAL_Y.extend([4, 5])
		Node.goal_a = tuple([(y, Node.goal_ax) for y in Node.GOAL_Y])
		Node.goal_b = tuple([(y, Node.goal_bx) for y in Node.GOAL_Y])
		Node.goal_c = tuple([(y, Node.goal_cx) for y in Node.GOAL_Y])
		Node.goal_d = tuple([(y, Node.goal_dx) for y in Node.GOAL_Y])
		Node.goals = [Node.goal_a, Node.goal_b, Node.goal_c, Node.goal_d]
		print(f'part={part}')
		print(f'Node.goals = {Node.goals}')

	def gethash(self):
		return tuple(sorted(self.a)) + tuple(sorted(self.b)) + tuple(sorted(self.c)) + tuple(sorted(self.d))

	def __lt__(self, other):
		return (self.f(), self.h, self.g, self.tiebreaker) < (other.f(), other.h, other.g, other.tiebreaker)

	def __iter__(self):
		for amphipod in [self.a, self.b, self.c, self.d]:
			yield amphipod

	def __getitem__(self, item: int) -> list[tuple[int, int], tuple[int, int]]:
		if item < -1 or item >= 4:
			raise IndexError
		return [self.a, self.b, self.c, self.d][item]

	def get_amphipods(self):
		for pos, goal in zip(self.__iter__(), Node.goals):
			yield pos, goal

	def heuristic(self):
		print(self)
		self.h = 0
		for i, (positions, goals) in enumerate(self.get_amphipods()):
			print(f'{i}')
			for pos, goalpos in zip(sorted(list(positions)), sorted(list(goals))):
				print(f'pos={pos}, goalpos={goalpos}')
				extra = Node.calc_distance(pos, goalpos) * (10 ** i)
				print(f'extra={extra}')
				self.h += extra
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
					Node.grid[y][x] = '.'
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
		s += f'Cost: {self.g}\n'
		s += f'Heuristic: {self.h}\n'
		return s

	def has_strays(self, pos, amphi_type) -> bool:
		y, x = pos
		other_types = [0, 1, 2, 3]
		other_types.remove(amphi_type)
		for cy in range(Node.GOAL_Y[-1], y, -1):
			for other_type in other_types:
				if (cy, x) in self[other_type]:
					return True
		return False

	def get_possible_moves(self, curr_pos, amphi_type):
		moves = set()
		seen = set()

		if curr_pos in Node.goals[amphi_type] and not self.has_strays(curr_pos, amphi_type):
			# Amphipod is already done, why move?
			return moves

		def prune():
			pruned = set()
			for move in moves:
				y, x = move
				try:
					if y >= 2:
						assert move in Node.goals[amphi_type]
						# Amphipods will never move from the hallway into a room unless that room is their destination room
						assert not self.has_strays(move, amphi_type)
						# And that room contains no amphipods which do not also have that room as their own destination.
					assert move not in Node.doors
					# Amphipods will never stop on the space immediately outside any room.
					assert not (curr_pos[0] == 1 and y == 1)
					# Once an amphipod stops moving in the hallway, it will stay in that spot until it can move into a room.
					pruned.add(move)
				except AssertionError:
					continue
			if pruned:
				print(f'{curr_pos}=>{sorted(list(pruned))}')
			return pruned

		def getneighbours(pos):
			neighs = set()
			for n in get_neighbours():
				new_pos = tuple(map(operator.add, pos, n))
				if new_pos in seen:
					continue
				y, x = new_pos
				if -1 in new_pos or Node.grid[y][x] == '#' or any(new_pos in pods for pods in self.__iter__()):
					continue
				seen.add(new_pos)
				neighs.add(new_pos)
				neighs.update(getneighbours(new_pos))
			return neighs
		moves.update(getneighbours(curr_pos))
		return prune()

	@staticmethod
	def calc_distance(pos: tuple, target: tuple) -> int:
		manh_dist = tuple(map(abs, tuple(map(operator.sub, target, pos))))
		if pos[0] >= 2 and target[0] >= 2 and pos[1] != target[1]:  # Gotta walk around the wall
			_, xdist = manh_dist
			ydist1 = pos[0] - 1
			ydist2 = target[0] - 1
			return xdist + ydist1 + ydist2
		return sum(manh_dist)

	def perform_moves(self):
		for amphi_type, amphipods in enumerate(self.__iter__()):
			for amphi_idx, amphi in enumerate(amphipods):
				possiblemoves = self.get_possible_moves(amphi, amphi_type)
				for target_pos in possiblemoves:
					new_node = Node(self)
					listy = new_node[amphi_type]
					listy[amphi_idx] = target_pos
					new_node.g += (10 ** amphi_type) * Node.calc_distance(amphi, target_pos)
					new_node.heuristic()
					yield new_node


def pathfind(start: Node) -> Node:
	print(f'LETS START PATHFINDING')
	closed_queue = {}
	open_queue = []
	heapq.heappush(open_queue, start)
	while len(open_queue) > 0:
		node = heapq.heappop(open_queue)
		print(f'Popping:\n{node}')
		if node.h == 0:
			return node
		nodehash = node.gethash()
		if nodehash in closed_queue.keys() and node.h > closed_queue[nodehash]:
			continue
		for move in node.perform_moves():
			hashy = move.gethash()
			if hashy in closed_queue.keys() and closed_queue[hashy] <= move.g:
				continue
			heapq.heappush(open_queue, move)
		nodehash = node.gethash()
		if nodehash not in closed_queue.keys() or closed_queue[nodehash] > node.h:
			closed_queue[node.gethash()] = node.h
	return None


def print_history(node: Node) -> None:
	if node.parent is not None:
		print_history(node.parent)
	print(node)


def parse(fstr: str, part: int = 1) -> Node:
	with open(fstr, 'r') as f:
		rows = f.read().splitlines()
		grid = [[c for c in r] for r in rows]
	if part == 2:
		grid.insert(3, [c for c in '  #D#C#B#A#'])
		grid.insert(4, [c for c in '  #D#B#A#C#'])
	Node.setgoals(part=part)
	Node.grid = copy.deepcopy(grid)
	for row in Node.grid:
		print(f'{row}')
	return Node.replace_amphipods()


def main(fstr: str, part: int = 1):
	global tiebreaker
	tiebreaker = 0
	start = parse(fstr, part)
	print(start.h)
	exit()
	ans = pathfind(start)
	print_history(ans)
	return ans.g


if __name__ == '__main__':
	# assert main('example.txt') == 12521
	# print(f'Part1: {main("input.txt")}')
	assert main('example.txt', part=2) == 44169
	print(f'Part2: {main("input.txt", part=2)}')
