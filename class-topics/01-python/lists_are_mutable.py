list_1 = [1, 3, 6, 8, 0, 6, 3]
list_2 = [1, 5, 8, 3, 7]

print(5 * list_2)
print(list_1 + list_2)
print(1 in list_1)

result = list_1.sort()
print(result)
print(list_1)

list_1.reverse()
print(list_1)

a = [3, 1, 8]
b = a
b.sort()
print(b)
print(a)

a = [3, 1, 8]
b = [3, 1, 8]
print(id(a))
print(id(b))
b.sort()
print(b)
print(a)

a = [3, 1, 8]
b = a[:]
b.sort()
print(b)
print(a)

c = [1, 6, 8, 3]
result = sorted(c)
print(result)
print(c)

c = [1, 6, 8, 3]
result = list(reversed(c))
print(result)
print(c)

tuple_ = (1, 6, 8, 3)
result = sorted(c)
print(result)
print(c)

tuple_ = (1, 6, 8, 3)
# tuple_.sort(c)
print(result)
print(c)

