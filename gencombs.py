from itertools import combinations

n, r = 11 + 3, 3
combs = combinations(range(n), r)

for comb in combs:
	items = ['1'] * n
	for i in comb:
		items[i] = '+'

	print(*items, '  ', *map(len, ''.join(items).split('+')))
