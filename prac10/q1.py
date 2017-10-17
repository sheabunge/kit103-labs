
from itertools import product
from string import ascii_lowercase as letters


def gen_perms(alphabet, k, print_set=True):
	n = len(alphabet)

	print(f'From an alphabet of {alphabet!r}')

	expected = n ** k
	print(f'{expected} permutations of P({n}, {k}) are expected (as letters can be repeated)')

	if k == 2:
		manually = {a + b for a in alphabet for b in alphabet}
		print(f'{len(manually)} permutations of P({n}, {k}) were found using set comprehensions')

	with_product = {''.join(p) for p in product(alphabet, repeat=k)}
	print(f'{len(with_product)} permutations of P({n}, {k}) were found using product()')

""" 1. Permutations with replacement """

gen_perms(letters, 2, True)
print()

""" 1.1 Strange creatures """

gen_perms('ATGC', 9, False)
