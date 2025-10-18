def by_element(my_list):
    for e in my_list:
        print(e)

def by_index(my_list):
    for i in range(0, len(my_list)):
        print(my_list[i])

# def with_while(my_list):

#     i = 0

#     while True:
#         print(my_list[i])
#         i = i + 1

#         if i == len(my_list):
#             break

def with_while(my_list):

    i = 0

    while i < len(my_list):
        print(my_list[i])
        i = i + 1
        

my_list = ["a", "b", "c", "d"]

# by_element(my_list)
# by_index(my_list)
with_while(my_list)