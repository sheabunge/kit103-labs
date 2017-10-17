from itertools import combinations, permutations, product
from scipy.misc import comb, factorial


def fact(n):
	return factorial(n, exact=True)


""" 1 Permutations with repeated elements """

n_copies = (1, 3, 4, 2)
n_books = sum(n_copies)

n_perms = fact(n_books) // (fact(1) * fact(3) * fact(4) * fact(2))

print(f'there are {n_perms} total permutations (from {n_books} books)')

titles = 'A' * 1 + 'B' * 3 + 'C' * 4 + 'D' * 2

perms = list(permutations(titles))
print(f'there are {len(perms)} total permutations using permutations()')

perms_set = set(permutations(titles))
print(f'there are {len(perms)} total permutations using permutations() as a set')

