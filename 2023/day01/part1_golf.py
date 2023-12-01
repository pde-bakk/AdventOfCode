s=0
for l in open(0):d=[c for c in l if'/'<c<':'];s+=int(d[0]+d[-1])
print(s)
