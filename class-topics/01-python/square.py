def square_list(l):

	out_l = []

	for e in l:
		out_l.append(e ** 2)

	return out_l

l = [0, 1, 2, 3, 4, 5, 6, 7]

print(square_list(l))

print([e ** 2 for e in l])