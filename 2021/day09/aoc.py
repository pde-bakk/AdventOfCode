def is_basin(rows, y, x) -> bool:
	if (x > 0 and rows[y][x - 1] <= rows[y][x]) or (x < len(rows[y]) - 1 and rows[y][x + 1] <= rows[y][x]):
		return False
	if (y > 0 and rows[y - 1][x] <= rows[y][x]) or (y < len(rows) - 1 and rows[y + 1][x] <= rows[y][x]):
		return False
	return True


def part1(rows: list[list[int]]):
	total = 0
	for y, row in enumerate(rows):
		for x, item in enumerate(row):
			lowpoint = True
			if (x > 0 and row[x-1] <= item) or (x < len(row) - 1 and row[x+1] <= item):
				lowpoint = False
			if (y > 0 and rows[y-1][x] <= item) or (y < len(rows) - 1 and rows[y+1][x] <= item):
				lowpoint = False
			if lowpoint:
				total += item + 1
	return total


def part2(rows: list[list[int]]) -> int:  # returns the size of the basin
	def dfs(y_dfs: int, x_dfs: int):
		if y_dfs == -1 or x_dfs == -1 or y_dfs == len(rows) or x_dfs == len(rows[0]):
			return 0
		if (y_dfs, x_dfs) in seen:
			return 0
		value = 1
		seen.add((y_dfs, x_dfs))
		curr = rows[y_dfs][x_dfs]
		for n in [(y_dfs-1,x_dfs), (y_dfs+1,x_dfs),(y_dfs, x_dfs-1), (y_dfs, x_dfs+1)]:
			if -1 in n or n[0] == len(rows) or n[1] == len(rows[0]):
				continue
			if rows[n[0]][n[1]] > curr and rows[n[0]][n[1]] != 9:
				value += dfs(n[0], n[1])
		return value

	basins = []
	for y, row in enumerate(rows):
		for x, item in enumerate(row):
			if is_basin(rows, y, x):
				seen = set()
				val = dfs(y, x)
				basins.append(val)
	basins = sorted(basins, reverse=True)[:3]
	print(basins)
	return basins[0] * basins[1] * basins[2]


if __name__ == '__main__':
	lines = open("input.txt").read().splitlines()
	grid = []
	for line in lines:
		grid.append([int(x) for x in line])

	print(f'Part1: {part1(grid)}')
	print(f'Part2: {part2(grid)}')
