set_1 = {1, 2, 1, 3}
set_2 = {1, 4}
set_3 = {2, 3}

print(set_1)

print(1 in set_1)
print(4 in set_1)

print(set_1.intersection(set_2))
print(set_1 & set_2)

print(set_1.union(set_2))
print(set_1 | set_2)

print(set_1.difference(set_2))
print(set_1 - set_2)

print(set_2.difference(set_1))
print(set_2 - set_1)

print(set_2.symmetric_difference(set_1))
print(set_2 ^ set_1)

empty_set = set()
print(empty_set)
print(type(empty_set))

set_5 = empty_set | {4}
print(set_5)
print(empty_set)
set_5 = empty_set | {3}
print(set_5)
print(empty_set)

def unique_chars(str_):
	# set_ = set()
	# for char in str_:
	# 	set_ = set_ | {char}
	# return set_
	return set(str_)

print(unique_chars("hello world"))


