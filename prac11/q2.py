from itertools import combinations, permutations, product
from scipy.misc import comb, factorial

"""
2 C(31, 2) flavours

Task: Baskin-Robbins reputedly sell 31 flavours of ice cream, although the true number is higher than that.
Assuming that they did only have 31 flavours on offer, how many different two-scoop ice creams are possible?
"""

n, r = 31, 2

n_combs = comb(n, r, exact=True)
print(f'the total number of {r} scoop combinations from {n} flavours is {n_combs}')

flavours = [l.strip() for l in open('br31.txt')]
double_scoops = None




