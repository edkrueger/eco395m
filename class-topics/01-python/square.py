def square(x):
    return x ** 2


def square_list(l):

    l_out = []

    for e in l:
        l_out += [square(e)]

    return l_out

l = [1, 2, 3]
print(square_list(l))
print(list(map(square, l)))
print(list(map(lambda x: x ** 2, l)))
print([e ** 2 for e in l])