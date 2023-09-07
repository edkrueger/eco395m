l = [5, 6, 3, 2, 5]

# # for loop by element
# for e in l:
#     print(e)

# for loop by index
# for i in range(len(l)):
#     print(l[i])

# while 1

i = 0
while i < len(l):
    print(l[i])
    i = i + 1

# while 2

i = 0
while i <= len(l) - 1:
    print(l[i])
    i = i + 1

# while 3

i = 0
while True:
    print(l[i])
    i = i + 1

    if i >= len(l):
        break

# range()
print(list(range(5)))
print(list(range(2, 5)))
print(list(range(2, 100, 2)))
