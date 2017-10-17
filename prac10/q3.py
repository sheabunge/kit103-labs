

def r_permute(items, r, temp=None, results=None):
	results = set() if results is None else results
	temp = [] if temp is None else temp

	if len(temp) == len(items):
		results.add(tuple(temp))
	else:
		for item in (item for item in items if item not in temp):
			temp.append(item)
			r_permute(items, temp, results)
			temp.remove(item)

	return results

if __name__ == '__main__':
	party = ('Alice', 'Bob', 'Charlie', 'Daphne')
	print(r_permute(party, 2))
