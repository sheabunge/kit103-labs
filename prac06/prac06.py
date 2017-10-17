from math import sqrt
from random import randrange

""" 1. Common divisibility rules and huge numbers """


def divisible_by_2(n):
	return int(n[-1]) % 2 == 0


def divisible_by_3(n):
	return sum(int(d) for d in n) % 3 == 0



def divisible_by_4(n):
	return sum(int(d) for d in n[-2:]) % 4 == 0


def divisible_by_5(n):
	return n[-1] in '05'


def divisible_by_7(n):

	while len(n) > 2:
		last, n = n[-1], n[-1:]

		n = int(n) - int(last) * 2
		n = str(n)

	return int(n) % 7 == 0


def divisible_by_9(n):
	return sum(int(d) for d in n) % 9 == 0


def divisible_by_11(n):
	m = []

	for i, d in enumerate(n):
		d = int(d)
		m.append(-d if i % 2 == 0 else d)

	return sum(m) % 11 == 0

""" 1.1 Generating test cases """


def test(d, cases=20, limit=10):
	func = globals()[f'divisible_by_{d}']

	for _ in range(cases):
		n = randrange(limit) + 2
		divides = n % d == 0

		if func(str(n)) != divides:
			print(f'Failure: {n} should {"not " if divides else ""}be divisible by {d}')


for d in (2, 3, 4, 5, 7, 9, 11):
	test(d)


def isprime(n):

	if n <= 1:
		return False

	if n <= 3:
		return True

	if n % 2 == 0 or n % 3 == 0:
		return False

	for i in range(5, int(sqrt(n)) + 1, 6):
		if n % i == 0 or n % (i + 2) == 0:
			return False

	return True
