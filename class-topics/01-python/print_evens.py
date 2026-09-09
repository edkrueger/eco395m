# def print_evens(upper):
# 	for num in range(0, upper, 2):
# 		print(num)

# print_evens(100)


# def print_evens(upper):
# 	for num in range(0, upper):
# 		if num % 2 == 0:
# 			print(num)

# print_evens(100)

def print_evens(upper):

	num = 1

	while num < upper:
		if num % 2 == 0:
			print(num)
		num = num + 1

print_evens(1000)