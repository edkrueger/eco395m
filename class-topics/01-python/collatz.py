def collatz_next(a_n):

	if a_n % 2 == 0:
		return a_n // 2
	else:
		return 3 * a_n + 1

def collatz(a_0):

	a = a_0

	print(a)

	while a != 1:
		a = collatz_next(a)
		print(a)

collatz(342621)

