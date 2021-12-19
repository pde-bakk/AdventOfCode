import numpy as np
import operator
from itertools import permutations


global scanners
global all_distances
flips = [(1, 1, -1), (1, -1, 1), (-1, 1, 1)]
rots = [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)]


def manhattan_distance(_a, _b) -> int:
	return abs(_a[0] - _b[0]) + abs(_a[1] - _b[1]) + abs(_a[2] - _b[2])


def diff(_a, _b):
	return np.array([_a[0] - _b[0], _a[1] - _b[1], _a[2] - _b[2]])


def get_rotation(_arr: np.ndarray) -> np.ndarray:
	"""Returns the whole array flipped and/or rotated"""
	for neg_perm in [[1, 1, 1], [1, 1, -1], [1, -1, 1], [1, -1, -1], [-1, 1, 1], [-1, 1, -1], [-1, -1, 1], [-1, -1, -1]]:
		for perm in [[0, 1, 2], [1, 2, 0], [2, 0, 1]]:
			a = _arr[:, perm]
			for _i, _neg in enumerate(neg_perm):
				a[:, _i] *= _neg
			yield a


def parse(filename: str):
	raw_scanners = open(filename).read().split('\n\n')
	scans = []
	for scanner in raw_scanners:
		beacon_coords = np.array([[int(x) for x in row.split(',')] for row in scanner.splitlines()[1:]])
		scans.append(beacon_coords)
	return scans


def get_all_dists():
	all_dists = []
	for scan in scanners:
		dists = []
		for point in scan:
			# Getting the distance from point to every other beacon
			# And saving it in 1 large numpy array for every beacon point
			# print(f'point={point}')
			absolutely = np.abs(scan - point)  # Creates an array [scan[0] - scan[0], scan[1] - scan[0], ..., scan[n] - scan[0]]
			# print(f'absolutely={absolutely}')
			summy = np.sum(absolutely, axis=1)  # Creates an array [sum(a[0]), sum(a[1]), ..., sum(a[2])]
			# print(f'summy={summy}')
			# summy = np.delete(summy, np.argwhere(summy == 0)) # doesnt work, since I do need to know where i and j are, nice try tho I guess
			dists.append(summy)
			# print(f'len dists = {len(dists)}, dists={dists}')
			# exit()
		all_dists.append(dists)
	return all_dists


def find_one_overlap(scan0: int, scan1: int) -> tuple:
	# print(f'length={len(all_distances[scan0])}')
	for i, d0 in enumerate(all_distances[scan0]):
		for j, d1 in enumerate(all_distances[scan1]):
			# Finds beacons i and j which are the same (because they have the same distances to at least 12 other beacons)
			# print(f'checking d0: {d0}\nandd1:{d1}')
			overlaps = set(d0) & set(d1)
			if len(overlaps) >= 12:
				return i, j, overlaps
	return None, None, None


def find_positions(known_idx, unknown_idx, b0_idx, b1_idx, overlaps):
	new_orient = np.ndarray
	print(f'known_idx={known_idx}, unknown_idx={unknown_idx}, b0_idx={b0_idx}, b1_idx={b1_idx}, overlaps={overlaps}')
	for d in overlaps:
		if d == 0:
			# Same distance to itself doesn't help us of course
			continue
		q0 = np.where(all_distances[known_idx][b0_idx] == d)[0][0]
		q1 = np.where(all_distances[unknown_idx][b1_idx] == d)[0][0]
		# Just like how b0_idx and b1_idx represent the same beacon as seen from different scanners,
		# q1 and q2 represent the same beacon
		# Because we now have 2 beacon locations, we can find the unknown_scanner's rotation
		print(f'q0={q0}, q1={q1}')

		known_diff = scanners[known_idx][b0_idx] - scanners[known_idx][q0]
		unkown_diff = scanners[unknown_idx][b1_idx] - scanners[unknown_idx][q1]
		print(f'known_diff={known_diff}, unkown_diff={unkown_diff}')

		# if len(set(np.abs(diff0))) < 3:
		# 	print(f'length too smol')
		# 	continue

		order = []
		sign = []

		try:
			for i in range(3):
				idx = np.where(np.abs(unkown_diff) == abs(known_diff[i]))[0][0]
				# Gotta line up the axes with known_scanner
				order.append(idx)
				sign.append(unkown_diff[idx] // known_diff[i])
			print(order, sign)

			new_orient = scanners[unknown_idx][:, order] * np.array(sign)
			# print(f'new_orient = {new_orient}')
			print(f'sign array = {np.array(sign)}')
			break
		except IndexError as e:
			print(f'Exception {e}')
			continue

	scanner_pos = scanners[known_idx][b0_idx] - new_orient[b1_idx]
	new_coords = new_orient + scanner_pos
	return scanner_pos, new_coords


def find_all_scanners(scanner_positions):
	global scanners
	amount_scanners = len(scanners)
	known_scanners = {0}
	count = 1

	while count < amount_scanners:
		known_scanner_idx = known_scanners.pop()
		# print(f's0={s0}')

		for unknown_scanner_idx in range(amount_scanners):
			if unknown_scanner_idx in scanner_positions.keys():
				continue
			overlaps = find_one_overlap(known_scanner_idx, unknown_scanner_idx)
			if any([a is None for a in overlaps]):
				continue
			# global scanners
			scanner_positions[unknown_scanner_idx], scanners[unknown_scanner_idx] = find_positions(known_scanner_idx, unknown_scanner_idx, overlaps[0], overlaps[1], overlaps[2])
			known_scanners.add(unknown_scanner_idx)  # Assumes there aren't 2 scanners that will match with scanner 0
			count += 1
			# exit()


def find_all_beacons():
	beacons = set()
	for scanner_beacons in scanners:
		beacons.update([tuple(beacon) for beacon in scanner_beacons])
	return beacons


def find_furthest_distance(scanner_positions):
	res = 0
	for k, v in scanner_positions.items():
		for k2, v2 in scanner_positions.items():
			abss = np.abs(v - v2)
			print(f'abs={abss}')
			summy = np.sum(np.sum(abss))
			print(f'sum = {summy}')
			# res = max(summy, res)
			res = max(res, np.sum(np.abs(v - v2)))
	return res


def main(filename: str) -> tuple:
	global scanners, all_distances
	scanners = parse(filename)
	all_distances = get_all_dists()
	scanner_positions = {0: np.array([0, 0, 0])}
	find_all_scanners(scanner_positions)
	beacons = find_all_beacons()
	print(f'length of beacons = {len(beacons)}')
	return len(beacons), find_furthest_distance(scanner_positions)


if __name__ == '__main__':
	with open('output.txt', 'w') as f:
		example_outcome = main('example.txt')
		print(f'example_outcome = {example_outcome}')
		assert example_outcome[0] == 79
		assert example_outcome[1] == 3621
		print(f'Part1: {main("input.txt")}')
		print(f'Part1: {main("input.txt")}')
