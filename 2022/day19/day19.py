import re
import copy
from collections import deque
import heapq
MAX_TIME = 24


class State:
	def __init__(self, resources: list, robots: list):
		self.resources = copy.copy(resources)
		self.robots = copy.copy(robots)
		self.time = 0
		self.tmp = [0] * 4

	def can_build(self, costs: list) -> list[bool]:
		return [
			self.resources[0] >= costs[0],
			self.resources[0] >= costs[1],
			self.resources[0] >= costs[2] and self.resources[1] >= costs[3],
			self.resources[0] >= costs[4] and self.resources[2] >= costs[5]
		]

	def generate_minerals(self) -> None:
		for i in range(4):
			self.resources[i] += self.robots[i]
		self.time += 1

	def start_building(self, i: int, costs: list, count: int) -> None:
		if i == 0 or i == 1:
			self.resources[0] -= costs[i] * count
		elif i == 2:
			self.resources[0] -= costs[2] * count
			self.resources[1] -= costs[3] * count
		elif i == 3:
			self.resources[0] -= costs[4] * count
			self.resources[2] -= costs[5] * count
		self.tmp[i] += count

	def build(self):
		for i in range(4):
			self.robots[i] += self.tmp[i]
			self.tmp[i] = 0

	def __lt__(self, other):
		if not isinstance(other, State):
			raise NotImplemented
		if self.resources != other.resources[-1]:
			return self.resources[-1] > other.resources[-1]
		return self.robots[::-1] > other.robots[::-1]


def get_robot_cost(costs: list):
	yield costs[0]
	yield costs[1]
	yield costs[2], costs[3]
	yield costs[4], costs[5]


def run_bfs_for_blueprint(costs: list[int]) -> int:
	start_state = State([0, 0, 0, 0], [1, 0, 0, 0])
	q = [start_state]
	max_geodes = 0

	while q:
		state = heapq.heappop(q)
		can_build = state.can_build(robot_costs)
		if can_build[3]:
			new_state = copy.deepcopy(state)
			new_state.start_building(3, costs, count=1)
			new_state.generate_minerals()
			new_state.build()
			heapq.heappush(q, new_state)
		elif can_build[2]:
			new_state = copy.deepcopy(state)
			new_state.start_building(2, costs, count=1)
			new_state.generate_minerals()
			new_state.build()
			heapq.heappush(q, new_state)
		else:
			if can_build[1]:
				new_state = copy.deepcopy(state)
				new_state.start_building(1, costs, count=1)
				new_state.generate_minerals()
				new_state.build()
				heapq.heappush(q, new_state)

			if can_build[0]:
				new_state = copy.deepcopy(state)
				new_state.start_building(0, costs, count=1)
				new_state.generate_minerals()
				new_state.build()
				heapq.heappush(q, new_state)
		state.generate_minerals()
		heapq.heappush(q, state)

	return max_geodes


with open('test.txt', 'r') as f:
	blueprints = f.read().splitlines()

part_1 = []
for blueprint in blueprints:
	blueprint_id, *robot_costs = list(map(int, re.findall(r'\d+', blueprint)))
	print(robot_costs)
	part_1.append(blueprint_id * run_bfs_for_blueprint(robot_costs))
	break
print(part_1)
print(f'Part 1: {sum(part_1)}')
