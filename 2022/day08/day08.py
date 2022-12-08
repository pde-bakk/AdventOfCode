with open('input.txt', 'r') as f:
	trees = [list(map(int, line)) for line in f.read().splitlines()]
X_MAX, Y_MAX = len(trees[0]), len(trees)


def check_visible(x: int, y: int, xjump: int, yjump: int) -> bool:
	# Part 1
	tree_height = trees[y][x]
	x += xjump
	y += yjump
	while 0 <= x < X_MAX and 0 <= y < Y_MAX:
		if trees[y][x] >= tree_height:
			return False
		x += xjump
		y += yjump
	return True


def get_trees(x: int, y: int, xjump: int, yjump: int) -> int:
	tree_height = trees[y][x]
	x += xjump
	y += yjump
	trees_visible = 0
	while 0 <= x < X_MAX and 0 <= y < Y_MAX:
		if trees[y][x] >= tree_height:
			trees_visible += 1
			break
		x += xjump
		y += yjump
		trees_visible += 1
	return trees_visible


def get_scenic_score(x: int, y: int) -> int:
	amount_trees = [get_trees(x, y, xj, yj) for yj, xj in [(-1, 0), (0, -1), (0, 1), (1, 0)]]
	return int(eval('*'.join(map(str, amount_trees))))


total_trees = 0
best_score = 0
for ty, line in enumerate(trees):
	for tx, tree in enumerate(line):
		if any(check_visible(tx, ty, xj, yj) for xj, yj in [(0, 1), (0, -1), (1, 0), (-1, 0)]):
			total_trees += 1
		best_score = max(best_score, get_scenic_score(tx, ty))
print(f'Part 1: {total_trees}')
print(f'Part 2: {best_score}')
