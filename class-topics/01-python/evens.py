def calc_evens(n):

    l = []

    for i in range(0, n):
        if i % 2 == 0:
            l += [i]

    return l

def calc_evens2(n):
    return list(range(0, n, 2))

def calc_evens3(n):

    l = []
    i = 0

    while i < n:
        if i % 2 == 0:
            l += [i]
        i += 1

    return l

print(calc_evens(10))
print(calc_evens2(10))
print(calc_evens3(10))



