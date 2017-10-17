from prac03.lab3 import words

""" 3. implementing own ∃ and ∀ """


def for_all(collection, predicate):

	for item in collection:
		if not predicate(item):
			return False

	return True


def for_all_simple(collection, predicate):
	return all(predicate(item) for item in collection)


def exists(collection, predicate):

	for item in collection:
		if predicate(item):
			return True

	return False


def exists_simple(collection, predicate):
	return any(predicate(item) for item in collection)


exists_tests = (
	({1, 2, 3, 4, 5}, lambda e: e == 4, True),
	({1, 2, 3, 5}, lambda e: e == 4, False),
)

for_all_tests = (
	({1, 2, 3, 4, 5}, lambda e: e < 5, False),
	({1, 2, 3, 4}, lambda e: e < 5, True),
)

for col, pred, expected in exists_tests:
	print()

