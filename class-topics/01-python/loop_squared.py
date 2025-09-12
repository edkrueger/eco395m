my_list = [1, 2, 3, 4, 5]

# def square(my_list):

#     out_list = []

#     for e in my_list:
#         out_list.append(e ** 2)

#     return out_list

# def square(my_list):

#     return [e ** 2 for e in my_list]

# def square_one(n):
#     return n ** 2

# def square(my_list):
#     return list(map(square_one, my_list))

def square(my_list):
    return list(map(lambda e: e**2, my_list))



print(square(my_list))

