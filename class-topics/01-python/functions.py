# fruitful (pure)

# def f(x):
# 	return x ** 3 - x ** 2 + 5

# print(f(1) == 5)
# print(f(-1) == 3)

# print(f(3))
# print(f(7))


# fruitless

# def add_one():
# 	global a
# 	a = a + 1

# a = 0

# print(a)
# add_one()
# add_one()
# add_one()
# print(a)


# def add(a, b):
# 	return a + b

# print(add(1, 1))

# print(add("cat", "duck"))

# print(add(1, "duck"))

# def is_even(n):
# 	return n % 2 == 0

# print(is_even(4) == True)
# print(is_even(21) == False)
# print(is_even(0) == True)


def get_letter_grade(num_grade):

	grade = None

	if num_grade >= 90:
		grade = "A" 
	elif num_grade >= 80:
		grade = "B"
	elif num_grade >= 70:
		grade = "C"
	elif num_grade >= 60:
		grade = "D"
	else:
		grade = "F"

	return grade

print(get_letter_grade(100) == "A")
print(get_letter_grade(73) == "C")
print(get_letter_grade(3) == "F" )




