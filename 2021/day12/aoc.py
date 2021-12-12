from copy import deepcopy


class Route:
	def __init__(self, curr: str):
		self.visited = [curr]
		self.current_node = curr
		self.visited_small_cave_twice = False

	def __deepcopy__(self, memodict={}):
		res = Route(self.current_node)
		res.visited = deepcopy(self.visited)
		return res

	def move(self, newnode: str) -> None:
		self.visited.append(newnode)
		self.current_node = newnode
		if not self.visited_small_cave_twice and any([node.islower() and self.visited.count(node) == 2 for node in self.visited]):
			self.visited_small_cave_twice = True


def parse_paths(rows: list[str]) -> dict:
	paths = dict()
	for row in rows:
		src, dst = row.split('-')
		if src not in paths:
			paths[src] = []
		if dst not in paths:
			paths[dst] = []
		if dst != 'start' and src != 'end':
			paths[src].append(dst)
		if src != 'start' and dst != 'end':
			paths[dst].append(src)
	return paths


def day12(rows: list[str], part: int, startnode='start') -> int:
	paths = parse_paths(rows)
	queue = [Route(startnode)]
	finished = []

	while queue:
		s = queue.pop(0)
		if s.current_node == 'end':
			# print(f'Found solid route: {s.visited}')
			finished.append(s)
		# print(f'currently on {s.current_node}, already visited {s.visited}')

		for n in paths[s.current_node]:
			if n not in s.visited or n.isupper() or (part == 2 and not s.visited_small_cave_twice):
				# print(f'appending {n}')
				newroute = deepcopy(s)
				newroute.move(n)
				queue.append(newroute)
	for i in finished:
		print(i.visited)
	return len(finished)


lines = open('input.txt').read().splitlines()
print(lines)
# print(f'Part 1: {day12(lines, 1)}')
print(f'Part 2: {day12(lines, 2)}')
