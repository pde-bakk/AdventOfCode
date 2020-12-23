myfile = [x for x in open('input', 'r').read().split('\n') if x != '']
all_allergens = dict()
all_ingredients = list()
ingredients = set()
for food in myfile:
	a, b = food[:-1].split('(contains ')
	ingrs, allergens = a.split(), b.split(', ')
	for alg in allergens:
		if alg not in all_allergens:
			all_allergens[alg] = list(ingrs)
		else:
			all_allergens[alg] = [x for x in ingrs if x in all_allergens[alg]]
	all_ingredients += ingrs
	ingredients.update(ingrs)

for alg in all_allergens:
	for item in all_allergens[alg]:
		if item in ingredients:
			ingredients.remove(item)
res = 0
for item in ingredients:
	res += all_ingredients.count(item)
print(f'Part 1:\n{res}')

repeat = True
while repeat:
	repeat = False
	for alg in all_allergens:
		if len(all_allergens[alg]) == 1:
			ingr = all_allergens[alg][0]
			for alg2 in all_allergens:
				if alg == alg2 or ingr not in all_allergens[alg2]: continue
				all_allergens[alg2].remove(ingr)
		else:
			repeat = True
print('Part2:\n' + ','.join([x for x in [all_allergens[k][0] for k in sorted(all_allergens)]]))
