import time


def test_prime(k, primes):
	for p in primes:
		if k % p == 0:
			return False
	return True


def primes1(n):
	primes = []
	for k in range(2, n+1):
		if test_prime(k, primes):
			primes.append(k)
	return primes


def primes2(n):
	primes = set(range(2, n+1))  # set of candidate primes

	for k in range(2, int(n ** 1/2) + 1):
		if k in primes:
			primes.difference_update(range(k ** 2, n + 1, k))
	return primes


def test_primes(pf, n, show_msg=True):
	start = time.clock()
	total = len(pf(n))
	elapsed = time.clock() - start

	if show_msg:
		print(f'Took {elapsed:g} seconds to produce the {total} primes up to {n}')

	return elapsed


for n in (10 ** i for i in range(1, 6)):
	test_primes(primes1, n)
	test_primes(primes2, n)
	print()


""" 2. Is it prime? """


def is_prime(n):
	n_root = int(n ** 1/2)
	primes = set(range(2, n_root + 1))

	for k in range(2, int(n_root ** 1/2) + 1):
		if k in primes:
			primes.difference_update(range(k ** 2, n + 1, k))

	primes = sorted(primes)

	for prime in primes:
		if n % prime == 0:
			return False

	return True


""" 2.1. Factorising compound numbers """


def prime_factors(n):
	primes = sorted(primes2(n))
	factors = []

	while n > 1:
		p = next(primes)
		while n % p == 0:
			n //= p
			factors.append(p)

