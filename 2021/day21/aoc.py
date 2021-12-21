import numpy as np
import functools
import operator


def parse(filename: str):
	rows = open(filename).read().splitlines()
	return int(rows[0][-1]), int(rows[1][-1])


def loop(player_pos: list[int, int]):
	print(f'player_pos={player_pos}')

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
		print(f'{rolls}.Player {pp+1} rolls {nbs} and moves to space {player_pos[pp]} for a total score of {scores[pp]}')
		turn += 3
	print(f'scores={scores}, turn = {rolls}')
	return min(scores) * rolls


def main(filename: str) -> tuple:
	p1, p2 = parse(filename)
	res1 = loop([p1, p2])
	return res1, 0


if __name__ == '__main__':
	example_outcome = main('example.txt')
	assert example_outcome[0] == 739785
	# assert example_outcome[1] == 0
	real_outcome = main('input.txt')
	print(f'Part1: {real_outcome[0]}')
	print(f'Part2: {real_outcome[1]}')
