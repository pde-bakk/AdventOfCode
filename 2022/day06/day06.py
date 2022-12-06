with open('input.txt', 'r') as f:
	line = f.read()


def find_start(s: str, size: int) -> int:
	for i in range(size, len(s)):
		if len(set(s[i - size: i])) == size:
			return i


print(f'First: {find_start(line, size=4)}')
print(f'Second: {find_start(line, size=14)}')
