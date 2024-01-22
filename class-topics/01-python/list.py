# my_list = [1, 1, 3, 3 , 4, 1, 2]
# my_mixed_list = [1, 1, 3, 3, "1231", 6j, 6.32412]
# my_matrix_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# print(my_matrix_list[1][0])
# print(my_mixed_list[0:4])
# print(my_mixed_list[5])
# print(my_list[::-1])
# print(my_list[:])

# print(my_list + my_mixed_list)
# print(1 in my_list)
# print(3.14 in my_list)
# print(3 * my_list)

# proof of mutation
# a = [1, 1, 3, 3 , 4, 1, 2]
# print(a)
# print(id(a))
# a.sort()
# print(a)
# print(id(a))

# # danger of mutation
# b = [1, 1, 3, 3 , 4, 1, 2]
# c = b
# c.reverse()
# print(c)
# print(b)

# # "safe" copy
# b = [1, 1, 3, 3 , 4, 1, 2]
# c = b[:]
# print(id(b))
# print(id(c))
# c.reverse()
# print(c)

# # the right way
# b = [1, 1, 3, 3 , 4, 1, 2]
# c = list(reversed(b))
# print(b)
# print(c)

# # the other right way
# b = [1, 1, 3, 3 , 4, 1, 2]
# c = b[::-1]
# print(b)
# print(c)


my_tuple = (1, 2, 3, 4)
tuple(reversed(my_tuple))
my_tuple[0]
my_tuple[0:1]