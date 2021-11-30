import math
array = open("abel.txt", "r").read().split('\n')
testcases = array[0].split(' ')
width = len(array[1])
length = len(array)
for k in range(len(testcases)):
    step_x, step_y = [int(m) for m in testcases[k].split('-')]
    testcases[k] = j = 0
    for i in range(1, length, step_y):
        if array[i][j] == '#':
            testcases[k] += 1
        j = (j + step_x) % width
print(math.prod(testcases))