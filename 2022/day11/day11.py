import copy


class Monkey:
	def __init__(self, text: list[str]):
		self.id = int(text[0].split()[-1].strip(':'))
		self.items = list(map(int, text[1].split(':')[1].strip().split(', ')))
		self.operation = text[2].split(' = ')[-1]
		self.test = int(text[3].split()[-1])
		self.true = int(text[4].split()[-1])
		self.false = int(text[5].split()[-1])
		self.throw_arr = [self.false, self.true]
		self.total = 0

	def __lt__(self, other) -> bool:
		if not isinstance(other, Monkey):
			return NotImplemented
		return self.total < other.total

	def __str__(self) -> str:
		return f'Monkey {self.id}: ' \
				f'{self.items=}, {self.test=}, {self.operation}, {self.true, self.false}\n'

	def throw_item(self, item: int, to):
		to.items.append(item)
		self.total += 1


with open('input.txt', 'r') as f:
	lines = f.read().split('\n\n')
g_monkeys = [Monkey(line.splitlines()) for line in lines]
modulo = eval('*'.join(map(str, [m.test for m in g_monkeys])))


def simulate(monkeys, iterations: int, part: int = 1) -> int:
	for i in range(iterations):
		for m_id, monkey in enumerate(monkeys):
			for old in monkey.items:
				new = eval(monkey.operation)
				if part == 1:
					new //= 3
				elif part == 2:
					new %= modulo
				to_idx = monkey.throw_arr[new % monkey.test == 0]
				monkey.throw_item(new, to=monkeys[to_idx])
			monkey.items.clear()
	monkeys.sort()
	return monkeys[-2].total * monkeys[-1].total


print(f'Part 1:', simulate(copy.deepcopy(g_monkeys), 20, part=1))
print(f'Part 2:', simulate(copy.deepcopy(g_monkeys), 10_000, part=2))
