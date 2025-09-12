my_list = [1, 2, 3, 4, 5]

# def my_sum(my_list):

#     total = 0

#     for e in my_list:
#         # total = total + e
#         total += e

#     return total

# def my_sum(my_list):

#     total = 0

#     for i in range(len(my_list)):
#         total += my_list[i]

#     return total

def my_sum(my_list):

    my_list_copy = my_list[:]

    total = 0

    while my_list_copy:
        total += my_list_copy.pop()
    
    return total


print(sum(my_list))
print(my_sum(my_list))
print(my_list)