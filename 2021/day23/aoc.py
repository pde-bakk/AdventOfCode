def parse(fstr: str):
	with open(fstr, 'r') as f:
		rows = f.read().splitlines()
		grid = [[c for c in r] for r in rows]
	return grid


def main(fstr: str):
	grid = parse(fstr)


if __name__ == '__main__':
	ret = main('example.txt')