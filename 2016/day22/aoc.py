import copy
import heapq
import operator
tiebreaker = 0
MAX_X = 0
MAX_Y = 0


class Node:
	def __init__(self, other=None):
		if other is None:
			self.size = self.used = self.available = self.use_pct = 0
		elif isinstance(other, str):
			fs, self.size, self.used, self.available, self.use_pct = other.split()
			other = fs.find('x')
			y = fs.find('y')
			self.x, self.y = int(fs[other + 1:y - 1]), int(fs[y + 1:])
			self.size = int(self.size[:-1])
			self.used = int(self.used[:-1])
			self.available = int(self.available[:-1])
			self.use_pct = int(self.use_pct[:-1])
		elif isinstance(other, Node):
			self.x, self.y = other.x, other.y
			self.size = other.size
			self.used = other.used
			self.available = other.available
			self.used = other.use_pct

	def __repr__(self) -> str:
		s = f'{self.y, self.x}, {self.used}T/{self.size}T'
		return s

	def __eq__(self, other) -> bool:
		return (self.y, self.x) == (other.y, other.x)

	def pos(self) -> tuple[int, int]:
		return self.y, self.x


class State:
	def __init__(self, x=None):
		if x is None:
			self.nodes = {}
			self.empty = (-1, -1)
			self.target = (-2, -2)
			self.g = 0  # Amount of moves
			self.h = 0  # Predicted distance to goalpos
		elif isinstance(x, State):
			self.nodes = copy.deepcopy(x.nodes)
			self.empty = x.empty
			self.target = x.target
			self.g = x.g
			self.h = x.h
		global tiebreaker
		self.tiebreaker = tiebreaker
		tiebreaker += 1

	def heuristic(self) -> int:
		# self.h = 0
		manh_dist = tuple(map(abs, map(operator.sub, self.target, (0, 0))))
		self.h = sum(manh_dist)
		return self.h

	def set_initial(self, nodes: list[Node]):
		for node in nodes:
			print(f'node at {node.pos()}')
			self.nodes[node.pos()] = node
			if node.used == 0:
				self.empty = node.pos()
			if node.x == 0 and node.y > self.target[0]:
				self.target = node.pos()
			global MAX_X, MAX_Y
			MAX_X = max(MAX_X, node.x)
			MAX_Y = max(MAX_Y, node.y)
		self.heuristic()

	def make_move(self, moveto: tuple[int, int]):
		empty, newempty = self.getempty(), self.get(moveto)
		print(f'moving {empty} to {newempty}')
		assert newempty.used <= empty.size
		empty.used, newempty.used = newempty.used, empty.used
		if moveto == self.target:
			self.target = self.empty
		self.empty = moveto
		self.g += 1
		self.heuristic()

	def __lt__(self, other) -> bool:
		return (self.g + self.h, self.h, self.g, self.tiebreaker) < (other.g + other.h, other.h, other.g, other.tiebreaker)

	def get(self, tup: tuple[int, int]) -> Node:
		return self.nodes[tup]

	def gettarget(self) -> Node:
		return self.get(self.target)

	def getempty(self) -> Node:
		return self.get(self.empty)


def parse(filename: str) -> list[Node]:
	rows = open(filename, 'r').read().splitlines()
	return [Node(row) for row in rows[1:]]


def p1(nodes: list[Node]) -> int:
	viable = 0
	for a in nodes:
		for b in nodes:
			if a == b or a.used == 0:
				continue
			viable += int(a.used <= b.available)
	return viable


def create_state(nodes: list[Node]) -> State:
	state = State()
	state.set_initial(nodes)
	return state


def get_neighbours(pos: tuple[int, int]) -> tuple[int, int]:
	for n in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
		newpos = tuple(map(operator.add, pos, n))
		if newpos[0] not in (-1, MAX_Y + 1) and newpos[1] not in (-1, MAX_X + 1):
			print(f'newpos = {newpos}')
			yield newpos


def p2(state: State) -> int:
	open_q = []
	heapq.heappush(open_q, state)
	# closed_q = {}
	i = 0
	while open_q:
		state = heapq.heappop(open_q)
		if state.h == 0:
			return state.g
		for move in get_neighbours(state.empty):
			try:
				newstate = State(state)
				newstate.make_move(move)
				heapq.heappush(open_q, newstate)
			except AssertionError:
				pass
		# if state.empty == (0, 1):
		# 	break
		print()

		i += 1


def main(fstr: str):
	nodes = parse(fstr)
	# ans_p1 = p1(nodes)
	state = create_state(nodes)
	ans_p2 = p2(state)
	return 0, ans_p2


if __name__ == '__main__':
	print(f'Part: {main("example.txt")}')
