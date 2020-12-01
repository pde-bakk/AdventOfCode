
import sys

inputfile = open("day01/input", 'r')
Lines = inputfile.readlines()
nbs = list()

count = 0
for line in Lines:
    nbs.append(int(line.strip()))

print(str(nbs))

for a in range(len(nbs)):
    for b in range(a):
        for c in range(b):
            if nbs[a] + nbs[b] + nbs[c] == 2020:
                print("a is {}, b is {}, c is {}, multiplied they are {}".format(nbs[a], nbs[b], nbs[c], nbs[a] * nbs[b] * nbs[c]))
                exit()
