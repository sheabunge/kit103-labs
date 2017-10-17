from prac08.hash import *
from matplotlib import pyplot as plot

""" 3. hash functions """

words = [l.strip() for l in open('tlw.txt')]


def graph(size, h):
	dist = distribution(words, size, h)

	plot.bar(range(size), dist)
	plot.show()


for size in (10, 31):
	graph(size, java_hash)
	graph(size, py_hash)
