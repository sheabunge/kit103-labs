"""
For KIT103/KMA115 Practical 12: Modelling & Simulation
Revised: 2016-10-08
Authors: James Montgomery (james.montgomery@utas.edu.au),
         Malgorzata O'Reilly provided the original MATLAB scripts

Important usage notes for Spyder: When creating charts and other graphs,
Spyder's default behaviour is to render (draw) them inside the IPython
terminal. This makes the chart completely non-interactive and precludes
dynamically resizing it. If you'd like to be able to resize the charts
generated then you have two alternatives:

1. Select Consoles | Open a Python console from the menu. Then run this file
   and enter the various commands into the Python console instead of the
   IPython one.
OR
2. Close the IPython terminal in Spyder. Select Tools | Preferences from the
   menu. In the IPython section, select the Graphics tab, then change Graphics
   Backend from Inline to Automatic. Select Consoles | Open an IPython console
   for the changes to take effect. Run this file.
   (Note that you need to change this back if you want the inline drawing
   behaviour restored.)
"""

import numpy as np
from random import random, seed
from pylab import *


def restart_random_numbers(rs=1):
	"""Re-initialises the random number generator with the given
	random seed (default is 1), allowing for repeatable stochastic
	experiments.
	"""
	seed(rs)


# Simulating coin tosses

def coin_toss(n, p):
	"""Simulates the toss of a coin with P(heads) == p.
	Returns the number of heads observed over time in a list.
	"""
	heads = [0]  # initially no heads observed
	for i in range(n):
		if random() < p:
			heads.append(heads[-1] + 1)
		else:
			heads.append(heads[-1])
	return heads


def plot_coin_toss(n, p):
	"""Simulates the toss of a coin with P(heads) == p and plots the
	cumulative number of heads observed.
	"""
	x_n = coin_toss(n, p)
	plot_observations(x_n, 'Simulating toss of a coin with P(H)= {0:g}'.format(p))


def coin_toss_average(p, upto=1000):
	"""Performs `upto` independent runs of coin toss experiments,
	with 1, 2, ..., `upto` trials, and calculates the proportion of
	heads observed in each.
	Returns lists of the average and expected (i.e., p).
	"""
	x = []
	prob = []
	for n in range(1, upto + 1):
		x.append(coin_toss(n, p)[-1] / n)
		prob.append(p)
	return x, prob


def plot_coin_toss_average(p, upto=1000):
	"""Plots the observed average and expected probability of heads
	from `upto` independent coin toss experiments (of 1, 2, ...,
	`upto` trials each).
	"""
	x, prob = coin_toss_average(p, upto)
	plot_avg_and_expected(
		x, prob, event='coin tosses',
		plot_title='Simulating toss of a coin with P(H)= {0:g}'.format(p)
	)


# Simulating die rolls

def die_roll(n, sides=6, probs=None):
	"""Simulate n rolls of a die using a roulette wheel approach.
	Default, fair probabilities may be overridden by providing a
	list or tuple of same length as number of sides (default is 6)
	that contains the probabilities of the sides in order.
	Returns both the list of observations and probabilities used.
	"""
	if probs is None or len(probs) != sides:
		probs = (1 / sides,) * sides  # assume fair die
	assert abs(1 - sum(probs)) < 1e-10, 'sum(probs) == {0} != 1'.format(sum(probs))

	obs = []

	for i in range(n):
		r = random()
		total = 0
		side = 0
		while total < r:  # i.e., while we haven't yet found side selected
			total += probs[side]
			side += 1
		obs.append(side)
	return obs, probs


def plot_die_roll(n, sides=6, probs=None):
	"""Simulates the roll of a die and plots the side rolled in each
	trial. (Note that a line plot is not _entirely_ appropriate for
	this data, as each trial is independent of the others.)
	"""
	x_n, probs = die_roll(n, sides, probs)
	prob_string = ', '.join(['{0:1.3g}'.format(p) for p in probs])
	plot_observations(x_n, 'Roll of a die with p_i=' + prob_string)


def plot_fair_die_average(sides=6, upto=1000):
	"""Plots the observed average and expected probability of one
	particular side coming up on a die from `upto` independent die
	roll experiments (of 1, 2, ..., `upto` trials each).
	"""
	x, prob = coin_toss_average(1 / sides, upto=upto)
	plot_avg_and_expected(
		x, prob, event='die rolls',
		plot_title='Simulating roll of a fair {0}-sided die with P(i)=1/{0} for i=1,2,...,{0}'.format(sides)
	)


# Weather simulation

from enum import IntEnum


class Weather(IntEnum):
	"""An enumeration of the three weather states in the model.
	The use of the enum allows us to have more readable code, while
	still using these as indices into the transition matrix.
	"""
	sunny = 0
	rainy = 1
	cloudy = 2


# Sample transition probabilities
P1 = np.matrix([[0.4, 0.2, 0.4], [0.2, 0.5, 0.3], [0.4, 0.3, 0.3]])
P2 = np.matrix([[0.1, 0.4, 0.5], [0.2, 0.5, 0.3], [0.3, 0.4, 0.3]])


def simulate_weather(n, x0, P):
	"""Simulates the evolution of the weather over n days given a
	simple three-state model (sunny, rainy, cloudy), the initial
	state x0, and the transition probabilities given by P (a 3x3
	numpy array or matrix, in which P[i,j] is probability that
	tomorrow is state j given today is state i.
	"""
	history = [x0]

	for i in range(n):
		r = random()
		today = history[-1]
		# How might this approach be adapted to work with more states?
		# (Hint: think in terms of the state's number 0, 1, etc.)

		if r < P[today, Weather.sunny]:
			tomorrow = Weather.sunny
		elif r < P[today, Weather.sunny] + P[today, Weather.rainy]:
			tomorrow = Weather.rainy
		else:
			tomorrow = Weather.cloudy
		history.append(tomorrow)
		today = tomorrow

	return history


def plot_weather_simulation(n, x0, P):
	"""Simulates the evolution of weather over n days given our
	simple three-state model and initial state x0, and plots the
	state observed on each trial. (Note that a line plot _is_
	somewhat appropriate for this data, as each trial is dependent
	on the preceding one.)
	"""
	x_n = simulate_weather(n, x0, P)
	plot_observations(
		x_n,
		plot_title='Simulating evolution of the weather in Sandy Bay',
		xtitle='time n', ytitle='Weather state at time n'
	)


def simulate_weather_avgs(n, x0, P):
	"""Runs the weather simulation over n days, using initial state
	x0 and transition probabilities in P, then calculates total
	number of times each state is observed and running averages for
	each state. Returns the observations, totals and list of running
	averages.
	"""
	states = len(P)
	# note that initial state is _not_ included in the running average
	totals = [0 for i in range(states)]  # total times each state observed
	averages = [[0] for i in range(states)]  # running averages at each step

	history = simulate_weather(n, x0, P)

	# Analyse the outcomes of that simulation (ignoring day 0)
	for i in range(1, n + 1):
		state = history[i]
		totals[state] += 1
		for s in range(states):
			averages[s].append(totals[s] / i)
	return history, totals, averages


def plot_weather_evolution(n, x0, P):
	"""Runs the weather simulation using the given number of days n,
	initial state x0 and transition probabilities in P. Plots the
	daily observations and, in a separate plot, the running average
	of how often each state was observed.
	Returns an array of the final averages for all states.
	"""
	plot_title = 'Simulating evolution of the weather in Sandy Bay'
	xaxis = 'time n'

	obs, state_totals, state_averages = simulate_weather_avgs(n, x0, P)
	# Plot daily observations
	plot_observations(obs, plot_title=plot_title, xtitle=xaxis, ytitle='Weather state at time n')

	# Plot running averages for all weather states
	figure()
	x = list(range(len(obs)))
	xlim(0, len(obs))
	ylim(0, 1)
	xlabel(xaxis)
	ylabel('Proportion of time that state was observed')
	title(plot_title)
	for s in Weather:
		plot(x, state_averages[s], label=str(s) if isinstance(s, IntEnum) else 'State {0}'.format(s))
	legend()

	# The numpy array type supports this slicing operation much better than a list of lists
	return np.array(state_averages)[:, -1]


# Plotting utilities used by the above

def plot_observations(obs, plot_title=None, xtitle=None, ytitle=None,
					  marker_size=50, fill_markers=False):
	"""Generates a line + scatter plot of the given sequence of
	observations, assumed to start at observation 0. A default title
	is generated if none is provided. Marker size and whether or not
	markers are filled can optionally be changed.
	"""
	x = list(range(1, len(obs) + 1))
	xlim(0, len(obs) - 1)
	ylim(0, max(obs))
	plot(x, obs)
	scatter(
		x, obs, s=marker_size,
		facecolors='blue' if fill_markers else 'none',
		edgecolors='darkred'
	)
	xlabel('Observations' if xtitle is None else xtitle)
	ylabel('n' if ytitle is None else ytitle)
	title('Simulation results' if plot_title is None else plot_title)


def plot_avg_and_expected(obs_avg, probs, event=None, plot_title=None):
	"""Generates a line plot with two series, the observed average
	proportion of times an event is observed for a given number of
	trials (x-axis) and the expected probability of x occurring.
	"""
	x = list(range(len(obs_avg)))  # x coordinates for the two series
	xlim(1, len(obs_avg))
	ylim(0, 1)  # to make the relative size easier to judge between runs
	plot(x, obs_avg)
	xlabel('number n of {0}'.format('trials' if event is None else event))
	ylabel('average observed events / n')
	title('Simulation results' if plot_title is None else plot_title)
	plot(x, probs, 'r')
