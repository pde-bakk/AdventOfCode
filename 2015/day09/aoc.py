from typing import List
import itertools


def setuproutes(rows: List[str]):
	for row in rows:
		if row:
			src, _, dst, _, dist = row.split()
			routes.append((src, dst, int(dist)))
			routes_dists[f'{src}=>{dst}'] = int(dist)
			airports.update([src, dst])


def part2() -> int:
	everyposs = list(itertools.permutations(airports))
	minimum = 0
	for poss in everyposs:
		dist = 0
		print(poss)
		for i in range(len(poss) - 1):
			if f'{poss[i]}=>{poss[i + 1]}' in routes_dists:
				dist += routes_dists[f'{poss[i]}=>{poss[i + 1]}']
			else:
				dist += routes_dists[f'{poss[i + 1]}=>{poss[i]}']
		minimum = max(dist, minimum)
	return minimum


routes = []
routes_dists = {}
airports = set()
lines = open('input.txt', 'r').read().split('\n')
setuproutes(lines)
print(routes)
print(routes_dists)
print(part2())
