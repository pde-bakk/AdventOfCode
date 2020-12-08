lines = open("input", 'r').read().split("\n")
ll = accumulator = 0
s = set()

while ll < len(lines):
	operation, value = lines[ll].split()
	if ll not in s:
		s.add(ll)
	else:
		break
	if operation == "acc":
		accumulator += int(value)
		ll += 1
	elif operation == "jmp":
		ll += int(value)
	elif operation == "nop":
		ll += 1

print(accumulator)
