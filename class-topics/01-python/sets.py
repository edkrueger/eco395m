# some mutation
my_set = {1, 2, 3, 4, 4}
bad_copy = my_set

my_set.add(5)
my_set.remove(2)

# print(my_set)
# print(bad_copy)

# set operators

set_a = {1, 2, 3}
set_b = {3, 4, 5}

# print(set_a.union(set_b))
# print(set_a | set_b)

# print(set_a.intersection(set_b))
# print(set_a & set_b)

# print(set_a.difference(set_b))
# print(set_a - set_b)

# print(set_b.difference(set_a))
# print(set_b - set_a)

# print(set_b.symmetric_difference(set_a))
# print(set_b ^ set_a)

# no mutation
my_set = {1, 2, 3, 4, 4}

new_set = (my_set | {5}) - {2}

print(new_set)
print(my_set)
