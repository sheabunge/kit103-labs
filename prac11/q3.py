

def combins(items, r, i, c, results):
	if len(c) == r:
		results.add(set(c))
	elif i < len(items):
		c.add(items[i])
		combins(items, r, i + 1, c, results)
		c.remove(items[i])
		combins(items, r, i + 1, c, results)


items = 'ABCDE'
r = 3
results = set()
combins(items, r, 0, [], results)
