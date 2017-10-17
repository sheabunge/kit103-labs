
from prac03.bitsets import set2bits, bits2set

""" 1. Partitions and products """

""" 1.1 counting words """

words = {line.rstrip() for line in open('tlw.txt')}

# empty set, will only contain characters
ak = {w for w in words if w < '1'}

# will contain all words from the file
lz = {w for w in words if w >= '1'}

# words = lz
print(len(words), len(lz))
print()

""" 1.2 colour mixes """

colours = {'red', 'green', 'blue'}

colours_pairs = {(c1, c2) for c1 in colours for c2 in colours}
print('pairs with duplicates (length: {}):'.format(len(colours_pairs)))
print(colours_pairs)
print()

colours_pairs = {(c1, c2) for c1 in colours for c2 in colours if c1 != c2}
print('pairs without duplicates (length: {}):'.format(len(colours_pairs)))
print(colours_pairs)
print()

""" 1.3 deck of cards """

suits = {'♠', '♥', '♣', '♦'}
ranks = {'A', 'K', 'Q', 'J'} | set(range(2, 11))

cards = {(rank, suit) for rank in ranks for suit in suits}

print('number of cards:', len(cards))
print(cards)


""" 2. compact representations (bitsets) """

u = {'ant', 'bird', 'cat', 'dog', 'elk'}

00000

a = {'bird', 'dog'}
b = {'bird', 'cat', 'elk'}

a_bs = 0b01010
b_bs = 0b10110

print(bin(a_bs), bin(set2bits(a, u)))


