from collections import deque


class Route:
	def __init__(self, curr: str, visited=None, smallcave=False):
		self.current_node = curr
		if visited is None:
			self.visited = {curr}
		else:
			self.visited = visited.copy()
		self.visited_small_cave_twice = smallcave

	def move(self, newnode: str) -> None:
		if not self.visited_small_cave_twice and newnode.islower() and newnode in self.visited:
			self.visited_small_cave_twice = True
		self.visited.add(newnode)
		self.current_node = newnode


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
	queue = deque()
	queue.append(Route(startnode))
	finished = []

	while queue:
		s = queue.popleft()
		if s.current_node == 'end':
			finished.append(s)

		for n in paths[s.current_node]:
			if n not in s.visited or n.isupper() or (part == 2 and not s.visited_small_cave_twice):
				newroute = Route(s, s.visited, s.visited_small_cave_twice)
				newroute.move(n)
				queue.append(newroute)
	return len(finished)


lines = open('input.txt').read().splitlines()
print(f'Part 1: {day12(lines, 1)}')
print(f'Part 2: {day12(lines, 2)}')
