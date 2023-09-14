a = {1, 2, 3, 4, 5, 5}

print(a)
print(2 in a)

b = a.union({6, 8, 4})
c = b | {10, 20}
print(a)
print(b)
print(c)

x = {1, 2, 3, 4, 5}
y = {4, 5, 6, 7, 8}

print(x.intersection(y))
print(x & y)
print(x - y)
print(y - x)
print(x ^ y)
print(y ^ x)

z = {5, 4, 3, 2, 1}
print(z)
print(z == x)

empty = set()
print(empty)
print(type(empty))