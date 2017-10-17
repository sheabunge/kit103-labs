from prac04.truth_table import *

""" 2. testing and simplifying procedures """

predicates = (
	(
		'¬a ^ ¬b ^ ¬c',
		lambda a, b, c: not a and not b and not c,

		'¬(a v b v c)',
		lambda a, b, c: not (a or b or c),
	),
	(
		'a v (b ^ a)',
		lambda a, b, c: a or (b and a),

		'a',
		lambda a, b, c: a,
	),
	(
		'¬a v a',
		lambda a, b, c: not a or a,

		'1',
		lambda a, b, c: True
	),
	(
		'(a ^ b) v (¬a ^ b)',
		lambda a, b, c: (a and b) or (not a and b),

		'b',
		lambda a, b, c: b,
	),
	(
		'(a ^ b) v (a ^ c)',
		lambda a, b, c: (a and b) or (a and c),

		'a ^ (b v c)',
		lambda a, b, c: a and (b or c),
	)
)

for i, predicates in enumerate(predicates):
	print('-' * 4, i + 1, '-' * 4)
	print()

	exp, predicate, *predicates = predicates

	print(exp)
	truth_table(predicate, 3, True)
	print()

	if predicates:
		exp, predicate = predicates

		print(exp)
		truth_table(predicate, 3, True)
		print()
