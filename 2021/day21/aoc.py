import numpy as np
import functools
from collections import Counter, deque
import operator
import decorators


def parse(filename: str):
	rows = open(filename).read().splitlines()
	return int(rows[0][-1]), int(rows[1][-1])


def loop(player_pos: list[int, int]):

	def do_roll(p: int) -> str:
		nonlocal die, rolls
		roll_nbs = []
		for _ in range(3):
			if die > 100:
				die %= 100
			player_pos[p] += die
			roll_nbs.append(die)
			die += 1
			rolls += 1
		if player_pos[p] > 10:
			player_pos[p] %= 10
		if player_pos[p] == 0:
			player_pos[p] = 10
		scores[p] += player_pos[p]
		return '+'.join(map(str, roll_nbs))

	scores = [0, 0]
	die = 1
	turn = 0
	rolls = 0
	while scores[0] < 1000 and scores[1] < 1000:
		pp = turn % 2
		nbs = do_roll(pp)
		# print(f'{rolls}.Player {pp+1} rolls {nbs} and moves to space {player_pos[pp]} for a total score of {scores[pp]}')
		turn += 3
	return min(scores) * rolls


wins = [0, 0]
throws = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}


def diceroll() -> tuple[int, int]:
	for throw, amount in throws.items():
		yield throw, amount


def create_tuple(player_pos, scores, turn, throw, amount):

	def move(p):
		player_pos[p] += throw
		if player_pos[p] > 10:
			player_pos[p] %= 10
		scores[p] += player_pos[p]
	move(turn % 2)
	return player_pos, scores, turn + 1, amount


def play(pos, s, t):
	counter = Counter()
	queue = deque()
	queue.append((pos, s, t, 1))

	while len(queue) > 0:
		player_pos, scores, turn, amount = queue.pop()
		if any([score >= 21 for score in scores]):
			wins[scores[1] >= 21] += amount
			continue

		for throw, amount2 in diceroll():
			queue.append(create_tuple(player_pos.copy(), scores.copy(), turn, throw, amount * amount2))


def main(filename: str) -> tuple:
	p1, p2 = parse(filename)
	res1 = loop([p1, p2])
	play([p1, p2], [0, 0], 0)
	print(f'wins= {wins}')
	res2 = max(wins)
	return res1, res2


if __name__ == '__main__':
	# example_outcome = main('example.txt')
	# assert example_outcome[0] == 739785
	# assert example_outcome[1] == 444356092776315
	real_outcome = main('input.txt')
	print(f'Part1: {real_outcome[0]}')
	print(f'Part2: {real_outcome[1]}')
