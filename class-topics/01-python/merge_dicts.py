# not a pure function
# def merge_dicts(d1, d2):

# 	for k, v in d2.items():
# 		d1[k] = v

# 	return d1

# d1 = {"a": 1, "b": 2}
# d2 = {"c": 3, "a": 4}

# print(merge_dicts(d1, d2))
# print(d1)
# print(d2)

def merge_dicts(d1, d2):

	out_dict = {}

	for k, v in d1.items():
		out_dict[k] = v

	for k, v in d2.items():
		out_dict[k] = v

	return out_dict

d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "a": 4}

print(merge_dicts(d1, d2))
print(d1)
print(d2)

print({**d1, **d2})

l1 = [1, 2, 3]
l2 = [1, 2, 3]

print([*l1, *l2])

s1 = [1, 2, 3]
s2 = [1, 2, 4]

print({*s1, *s2})