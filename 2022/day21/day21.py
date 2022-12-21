def get_item(key: str):
	value = d[key]
	if value.isdigit():
		return value
	a, op, b = value.split()
	a_value, b_value = get_item(a), get_item(b)
	return eval(f'{a_value} {op} {b_value}')


with open('input.txt', 'r') as f:
	lines = f.read().splitlines()
	d = {}
	for line in lines:
		k, v = line.replace('/', '//').split(': ')
		d[k] = v

print(f'Part 1:', get_item('root'))
