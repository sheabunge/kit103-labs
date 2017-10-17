import string

""" 1. base 2 - 36 to decimal """


def q1():
	values = (('1010', 2), ('12', 8), ('A', 16), ('F00DCAFE', 16), ('ARGH', 36))

	for n, base in values:
		decimal_value = int(n, base)
		print(f'the decimal value of {n} (base {base}) is {decimal_value}')


""" 2. decimal to base 2 - 9 """


def dec2smaller(d, base):
	quotient, remainder = divmod(d, base)

	if quotient == 0:
		return str(remainder)

	return dec2smaller(quotient, base) + str(remainder)


def q2():
	tests = ((10, 2), (8, 8), (255, 2), (27, 3), (100, 9))
	for dec, base in tests:
		print(f'the decimal value {dec} in base {base} is {dec2smaller(dec, base)}')


""" 3. decimal to base 2 - 9 """

digits = string.digits + string.ascii_uppercase
print(digits)


def dec2other(d, base):
	quotient, remainder = divmod(d, base)

	if quotient == 0:
		return digits[remainder]

	return dec2other(quotient, base) + digits[remainder]


def q3():
	tests = ((10, 2), (121, 11), (10, 16), (4096, 16), (100, 20), (22569, 36))

	for dec, base in tests:
		print(f'the decimal value {dec} in base {base} is {dec2other(dec, base)}')


""" 3.1. Passing messages in class """


def q3_1():
	message = 'HelloR2D2'

	encoded = int(message, 36)
	print(f"'{message}' in base 36 is '{encoded}'")

	decoded = dec2other(encoded, 36)
	print(f'the decoded message is ', *decoded, sep='')

for q in (q1, q2, q3, q3_1):
	q()
	print()
