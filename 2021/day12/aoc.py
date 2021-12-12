from copy import deepcopy


class Route:
	def __init__(self, curr: str):
		self.visited = [curr]
		self.current_node = curr

	def __deepcopy__(self, memodict={}):
		res = Route(self.current_node)
		res.visited = deepcopy(self.visited)
		return res

	def move(self, newnode: str):
		self.visited.append(newnode)
		self.current_node = newnode


def parse_paths(rows: list[str]):
	paths = dict()
	for row in rows:
		src, dst = row.split('-')
		if src not in paths:
			paths[src] = []
		if dst not in paths:
			paths[dst] = []
		paths[src].append(dst)
		paths[dst].append(src)
	return paths


def part1(rows: list[str], startnode='start'):
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
			if n not in s.visited or n.isupper():
				# print(f'appending {n}')
				newroute = deepcopy(s)
				newroute.move(n)
				queue.append(newroute)
	return len(finished)


lines = open('input.txt').read().splitlines()
print(lines)
print(f'Part 1: {part1(lines)}')
