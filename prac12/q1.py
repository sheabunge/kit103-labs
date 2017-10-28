from prac12.modelling import coin_toss, plot_coin_toss, coin_toss_average, plot_coin_toss_average
from pylab import show

n_values = (10, 50)
p_values = (0.1, 0.5, 0.7)

for n in n_values:
	for p in p_values:
		plot_coin_toss(n, p)
		show()
		plot_coin_toss(n, p)
		show()

