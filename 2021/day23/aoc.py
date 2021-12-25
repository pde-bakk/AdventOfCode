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
	#          y, x ,  y, x
	goal_a = ((2, 3), (3, 3))
	goal_b = ((2, 5), (3, 5))
	goal_c = ((2, 7), (3, 7))
	goal_d = ((2, 9), (3, 9))
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
		for pos, goal in zip(self.__iter__(), [Node.goal_a, Node.goal_b, Node.goal_c, Node.goal_d]):
			yield pos, goal

	def heuristic(self):
		self.h = 0
		# print(self)
		for i, (positions, goals) in enumerate(self.get_amphipods()):
			# for pos in positions:
			# 	# print(f'pos={pos}, goals={goals}')
			# 	dist1 = Node.calc_distance(pos, goals[0])
			# 	dist2 = Node.calc_distance(pos, goals[1])
			# 	minimum = min(dist1, dist2)
			# 	# print(f'dist1={dist1}, dist2={dist2}, min={minimum}')
			# 	self.h += minimum
			for pos, goalpos in zip(sorted(list(positions)), sorted(list(goals))):
				self.h += Node.calc_distance(pos, goalpos) * (10 ** i)
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

	def move_is_possible(self, movetile) -> bool:
		if any(c == -1 for c in movetile):
			return False
		my, mx = movetile
		if Node.grid[my][mx] == '#':
			return False
		if any(movetile in x for x in [self.a, self.b, self.c, self.d]):
			return False
		return True

	def get_possible_moves(self, curr_pos, amphi_type, amphi_idx):
		moves = set()
		seen = set()

		if curr_pos in Node.goals[amphi_type] and (curr_pos[0] == 3 or self[amphi_type][amphi_idx - 1] == (curr_pos[0] + 1, curr_pos[1])):
			# Amphipod is already done, why move?
			return moves

		def prune():
			pruned = set()
			for move in moves:
				y, x = move
				if y >= 2:
					# print(f'checking if {curr_pos} can move to {move}')
					if move not in Node.goals[amphi_type]:
						# print(f'cant cus not goal')
						continue  # Amphipods will never move from the hallway into a room unless that room is their destination room
					if y == 2:
						# print(f'other of same type @{self[amphi_type][amphi_idx-1]} ?== {y+1, x}')
						if self[amphi_type][amphi_idx - 1] != (y + 1, x):
							# print(f'Cant cus other st')
							continue  # and that room contains no amphipods which do not also have that room as their own destination.
					# print(f'AND HE CAN! POG')
				if move in Node.doors:
					continue  # Amphipods will never stop on the space immediately outside any room.
				if curr_pos[0] == 1 and y == 1:
					continue  # Once an amphipod stops moving in the hallway, it will stay in that spot until it can move into a room.
				# if curr_pos == (2, 9) and move == (1, 8):
				# 	print(f'actually does the move')
				pruned.add(move)
			# if pruned:
			# 	print(f'{curr_pos} can move to {sorted(list(pruned))}')
			return pruned

		def getneighbours(pos):
			neighs = set()
			for n in get_neighbours():
				new_pos = tuple(map(operator.add, pos, n))
				if new_pos in seen:
					continue
				y, x = new_pos
				if -1 in new_pos or Node.grid[y][x] == '#' or any(new_pos in x for x in self.__iter__()):
					continue
				seen.add(new_pos)
				neighs.add(new_pos)
				neighs.update(getneighbours(new_pos))
			return neighs
		moves.update(getneighbours(curr_pos))
		return prune()

	@staticmethod
	def manh(pos: tuple, target: tuple) -> int:
		manh_dist = tuple(map(abs, tuple(map(operator.sub, target, pos))))
		return sum(manh_dist)

	@staticmethod
	def calc_distance(pos: tuple, target: tuple) -> int:
		manh_dist = tuple(map(abs, tuple(map(operator.sub, target, pos))))
		total_dist = sum(manh_dist)
		if pos[0] >= 2 and target[0] >= 2 and pos[1] != target[1]:  # Gotta walk around the wall
			total_dist += 2
			if pos[0] == 3 and target[0] == 3:
				total_dist += 2
		return total_dist

	def perform_moves(self):
		for amphi_type, amphipods in enumerate(self.__iter__()):
			for amphi_idx, amphi in enumerate(amphipods):
				possiblemoves = self.get_possible_moves(amphi, amphi_type, amphi_idx)
				for target_pos in possiblemoves:
					ay, ax = amphi
					if amphi in Node.goals[amphi_type] and (Node.grid[ay + 1][ax] == '#' or amphipods[amphi_idx - 1] == (amphi[0] + 1, amphi[1])):
						# Amphipod is already in goal position, don't move
						continue
					# target_pos = tuple(map(operator.add, amphi, n))
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
	mini = float('inf')
	heapq.heappush(open_queue, start)
	while len(open_queue) > 0:
		node = heapq.heappop(open_queue)
		if node.h == 0:
			# mini = min(mini, node.g)
			# print(f'mini={mini}')
			# continue
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
	print(f'open_queue still has a length of {len(open_queue)}')
	print(f'closed queue has {len(closed_queue)} items in it')
	return None


def print_history(node: Node) -> None:
	if node.parent is not None:
		print_history(node.parent)
	print(node)


def parse(fstr: str) -> Node:
	with open(fstr, 'r') as f:
		rows = f.read().splitlines()
		grid = [[c for c in r] for r in rows]
	Node.grid = copy.deepcopy(grid)
	return Node.replace_amphipods()


def main(fstr: str):
	start = parse(fstr)
	ans = pathfind(start)
	print_history(ans)
	return ans.g


if __name__ == '__main__':
	# assert main('example.txt') == 12521
	print(f'Part1: {main("input.txt")}')
