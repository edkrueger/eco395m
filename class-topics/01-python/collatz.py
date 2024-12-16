def collatz(start):

	sequence = []

	current = start

	sequence.append(start)
	
	while current != 1:
		if current % 2 == 0:
			next_ = current // 2
		else:
			next_ = 3 * current + 1

		sequence.append(next_)
		current = next_

	return sequence

print(collatz(111))


