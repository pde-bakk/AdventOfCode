import copy
import heapq
import operator
import math
import numpy
import functools
from collections import deque


def parse(fstr: str):
	with open(fstr, 'r') as f:
		parts = f.read().split('inp w\n')
	res = []
	for part in parts:
		ppres = []
		rows = part.splitlines()
		for i, row in enumerate(rows):
			items = row.split(' ')
			if i in [3, 4, 14]:
				ppres.append(int(items[2]))
		if ppres:
			res.append(ppres)
	return res


def optim(parts: list[list[int]], model_nb: list[int]) -> bool:
	z = 0
	for i in range(14):
		w = model_nb[i]
		x = int((z % 26) + parts[i][1] != w)
		z //= parts[i][0]
		z *= 25 * x + 1
		z += (w + parts[i][2]) * x
	return z == 0


def main(fstr: str):
	pp = parse(fstr)
	for p in pp:
		print(p)
	for model_nb in range(9999993100000, 1111111111111, -1):
		if model_nb % 100000 == 0:
			print(f'model_nb={model_nb}')
		with open('answers.txt', 'a') as f:
			if optim(pp, [int(x) for x in str(model_nb)]):
				f.write(f'got valid thingy for {model_nb}\n')
				print(f'got valid thingy for {model_nb}')
		# break
	return 0


if __name__ == '__main__':
	ret = main('input.txt')
