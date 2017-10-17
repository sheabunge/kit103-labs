"""
For KIT103/KMA115 Practical 5: K-maps
Revised: 2015-08-01
Author: James Montgomery (james.montgomery@utas.edu.au)

The plot_kmap function can create visualisations of K-maps for Boolean
expressions of 2-4 variables. In practice you would just write these
down on paper, but this *kind* of visualisation is used in other
settings, too. Also included are three sample K-maps for plotting.

There is also a function, broken_if, with an overly complex Boolean
expression for you to simplify.
"""

from pylab import array, matplotlib, pcolor, rc, xlabel, ylabel
import matplotlib.ticker as ticker
import matplotlib.pyplot as plt

sample_kmap4 = [
	[0, 0, 1, 1],
	[0, 0, 1, 1],
	[1, 1, 0, 0],
	[0, 0, 1, 1]
]

sample_kmap3 = [
	[1, 0, 0, 1],
	[1, 1, 1, 1]
]

sample_kmap2 = [
	[1, 0],
	[1, 1]
]


def plot_kmap(kmap, axis_labels=('AB', 'CD')):
	"""Creates a colour map plot of the given K-map, described as a
	list of lists, written in the same order as the K-map would be
	drawn on paper. The axis labels can be changed by providing an
	alternative pair (i.e., a 2-tuple) of labels.
	"""
	# Creates the basic plot of coloured squares
	color_map = pcolor(array(kmap), cmap=_palette)
	# Tinkers with the settings to make it look 'right'
	_format_ticks(color_map.axes.xaxis, variables=len(kmap[0]) // 2)
	_format_ticks(color_map.axes.yaxis, variables=len(kmap) // 2)
	rc('font', size=16)
	xlabel(axis_labels[0])
	ylabel(axis_labels[1])
	plt.grid(which='major', linestyle='-')
	plt.gca().invert_yaxis()
	plt.show()


def broken_if(child, short, asthma):
	"""The if statement in this function is too complex! Simplify it."""
	if not asthma and not (child or short):
		print('You may board the Whirlwind')
		return True
	else:
		print('Sorry, you may not board the Whirlwind')
		return False


def sum_n_squares(n):
	if n == 1:
		return 1
	return n ** 2 + sum_n_squares(n - 1)

######################################################################
# 'Private' helper functions and definitions

_palette = matplotlib.colors.ListedColormap(['w', 'b'])
_tick_formatters = [
	ticker.FixedFormatter(['0', '1']),
	ticker.FixedFormatter(['00', '01', '11', '10'])
]


def _format_ticks(axis, variables=2):
	axis.set_ticks(list(range(0, 2 * variables)))
	axis.set_major_formatter(ticker.NullFormatter())
	axis.set_minor_locator(ticker.FixedLocator([x + 0.5 for x in range(0, 2 * variables)]))
	axis.set_minor_formatter(_tick_formatters[variables - 1])
