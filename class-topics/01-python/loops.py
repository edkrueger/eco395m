l = [1, 3, 5, 7, 11, 13, 17]

# print every element in a list

# for e in l:
#     print(e)

# for i in range(len(l)):
#     print(l[i])

# idx = 0
# while idx < len(l):
#     print(f"{idx=}")
#     print(f"{l[idx]=}")
#     idx = idx + 1

# print evens

# def evens_range(end):
#     for num in range(0, end, 2):
#         print(num)

# def evens_mod(end):
#     for num in range(0, end):
#         if num % 2 == 0: 
#             print(num)

# def evens_while(end):

#     num = 0

#     while num < end:
#         print(num)
#         num = num + 2

# evens_range(100)
# evens_mod(100)
# evens_while(100)

print(sum(l))

def total(l):

    result = 0

    for e in l:
        result = result + e

    return result

def total_idx(l):

    result = 0

    for i in range(len(l)):
        result = result + l[i]

    return result

def total_while(l):

    result = 0

    idx = 0

    while idx < len(l):
        result = result + l[idx]
        idx = idx + 1

    return result

print(total(l))
print(total_idx(l))
print(total_while(l))

# scalar multiplication

def scalar_mult(scalar, list_):

    out_list = []

    for e in l:
        out_list.append(e * scalar)

    return out_list

print(scalar_mult(5, l))

print([5 * e for e in l])
print([i for i in range(100) if i % 2 == 0])

def mult5(x):
    return 5 * x

print(list(map(mult5, l)))

print(list(map(lambda x: 5 * x
, l)))

r = (5 * e for e in l)
print(type(r))
print(r)

print(next(r))
print(next(r))

for e in r:
    print(e)
for e in r:
    print(e)






