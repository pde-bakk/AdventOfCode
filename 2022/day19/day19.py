import re
from collections import deque


def get_robot_cost(costs: list):
	yield costs[0]
	yield costs[1]
	yield costs[2], costs[3]
	yield costs[4], costs[5]


def run_bfs_for_blueprint(costs: list[int]) -> int:
	start = (0, 0, 0, 0, 0)  # 0 geodes, 0 obs, 0 clay, 0 ore, 0 minutes
	q = [start]
	max_geodes = 0

	while q:
		node = q.pop()
		for cost in get_robot_cost(costs):





with open('test.txt', 'r') as f:
	blueprints = f.read().splitlines()

for blueprint in blueprints:
	robot_costs = list(map(int, re.findall(r'\d+', blueprint)))
	print(robot_costs)
