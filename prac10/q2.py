from itertools import product, permutations
from string import ascii_lowercase
from math import factorial

""" 2 Permutations without replacement """


def gen_perms(alphabet, r):
	n = len(alphabet)

	using_fact = factorial(n) // factorial(n - r)
	print(f'{using_fact} permutations of P({n}, {r}) are expected using factorials (without replacement)')

	manually = n * (n - 1)
	print(f'{manually} permutations of P({n}, {r}) are expected (without replacement)')

	using_permutations = set(permutations(alphabet, r))
	print(f'{len(using_permutations)} permutations of P({n}, {r}) were found using permutations()')
	print()


""" 2.1 Two-letter words with distinct letters """

gen_perms(ascii_lowercase, r=2)

""" 2.2 Who’s in first? """

party = ('Alice', 'Bob', 'Charlie', 'Daphne')

gen_perms(party, r=len(party))
print()

# as only the first and last members matter, the middle members can be left unchanged
gen_perms(party, r=2)
print()
