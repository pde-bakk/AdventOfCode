s=0
for l in open(0):d=[*filter(str.isdigit,l)];s+=int(d[0]+d[-1])
print(s)
