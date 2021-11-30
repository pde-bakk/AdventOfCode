jolts = [int(x) for x in open("input", 'r').read().split("\n")]
jolts.append(0)
jolts.append(max(jolts) + 3)
jolts.sort()
S = {}


def dfs(i):
	if i + 1 == len(jolts):
		return 1
	if i in S: # Don't be doing no things twice, stupid
		return S[i]
	ret = 0
	for j in range(1, 4):
		if i + j < len(jolts) and jolts[i + j] - jolts[i] <= 3:
			ret += dfs(i + j)
	S[i] = ret
	return ret


print(dfs(0))
