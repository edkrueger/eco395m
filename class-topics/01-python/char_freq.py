def char_freq(str_):

	counts = {}

	for c in str_:
		if c in counts:
			counts[c] = counts[c] + 1
		else:
			counts[c] = 1

	return counts

print(char_freq("hello world"))

