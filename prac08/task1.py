
""" 1. Euclidean Algorithm """


def gcd(a, b):
	while a > 0:
		b, a = a, b % a
	return b

hobart_students = 114
laun_students = 36

n_groups = gcd(hobart_students, laun_students)
print(
	f'the {hobart_students} students in Hobart and {laun_students} in Launceston can be divided into {n_groups} groups.'
)

hobart_tute_sizes = [18, 20, 18, 16, 14, 12, 14]
laun_tute_sizes = [20, 16]
tute_sizes = set(hobart_tute_sizes + laun_tute_sizes)
gcds = {gcd(a, b) for a in tute_sizes for b in tute_sizes if a < b}
print(f'the largest group that can be made out of the tutorial groups {tute_sizes} is {min(gcds)}')


