lines = open("input", 'r').read().split("\n")
linenbs = list()
for ll in range(len(lines)):
	if "nop" in lines[ll] or "jmp" in lines[ll]:
		linenbs.append(ll)
while linenbs:
	accumulator = ll = 0
	s = set()
	cur = linenbs.pop()

	while ll < len(lines):
		if ll not in s:
			s.add(ll)
		else:
			print("found an instruction line weve already handled, ll=", ll)
			break

		operation, value = lines[ll].split()
		if ll == cur:
			operation = operation.replace('jmp', '%temp%').replace('nop', 'jmp').replace('%temp%', 'nop')
		if operation == "acc":
			accumulator += int(value)
			ll += 1
		elif operation == "jmp":
			ll += int(value)
		elif operation == "nop":
			ll += 1
		if ll == len(lines):
			print("We're at the end of the instruction file, accumulator has value {}".format(accumulator))
			exit()


print(accumulator)
