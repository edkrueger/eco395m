l = [1, 2, 3, 7, 5, 1]
a2 = l[:]
a3 = l

# print(l.sort())
# print(sorted(l))

l.append(9)

# print(l)
print(a2)
print(a3)

print(list(reversed(l)))

print(l + [9])

t = (1, 2, 3, 5)
print(t[-1])
print(t[1:3])

print((1, 2, 3) * 5)
print((1, 2, 3) + (5, 6))

print((1, 2, 3) + (5,))


print(tuple())