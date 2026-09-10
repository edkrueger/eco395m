set_0 = set()
set_1 = {1}
set_2 = {1, 2, 3}
set_3 = {1, 2, 3, 4 ,2}
set_4 = {1, 2, 3}
set_5 = {3, 4, 5}

print(set_3)

set_3.add(5)
set_3.remove(2)

print(set_4.intersection(set_5))
print(set_4 & set_5)

print(set_4.union(set_5))
print(set_4 | set_5)

print(set_4.difference(set_5))
print(set_4 - set_5)

print(set_5.difference(set_4))
print(set_5 - set_4)

print(set_5.symmetric_difference(set_4))
print(set_5 ^ set_4)

print(3 in set_5)
print(333 in set_5)

set_a = {1, 2, 3}
print(set_a | {4})