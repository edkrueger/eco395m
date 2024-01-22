def my_sum(l):
    
    sum_ = 0

    for e in l:
        sum_ += e

    return sum_

def my_sum1(l):
    
    sum_ = 0

    for i in range(len(l)):
        sum_ += l[i]

    return sum_

def my_sum2(l):
    
    sum_ = 0

    i = 0

    while i < len(l):
        sum_ += l[i]
        i += 1

    return sum_

print(sum([1, 2, 3, 4, 5, 6]))
print(my_sum([1, 2, 3, 4, 5, 6]))
print(my_sum1([1, 2, 3, 4, 5, 6]))
print(my_sum2([1, 2, 3, 4, 5, 6]))

