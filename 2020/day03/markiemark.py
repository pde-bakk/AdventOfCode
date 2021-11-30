terrain = open("abel.txt", "r").read().split("\n")
def find_trees(steps): return (sum(map(lambda x: terrain[x * steps[0]][(x * steps[1]) % len(terrain[0])] == '#', range(len(terrain) // steps[0]))))
print(find_trees([1, 1]) * find_trees([1, 3]) * find_trees([1, 5]) * find_trees([1, 7]) * find_trees([2, 1]))