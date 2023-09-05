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


# def get_letter_grade(num_grade):

# 	if  90 <= num_grade <= 100:
# 		return "A"
# 	if 80 <= num_grade < 90:
# 		return "B"
# 	if 70 <= num_grade < 80:
# 		return "C"
# 	if 60 <= num_grade < 70:
# 		return "D"
# 	if 0 <= num_grade < 60:
# 		return "F"

# 	raise ValueError("num_grade must be between 0 and 100 (inclusive)") 


# print(get_letter_grade(100) == "A")
# print(get_letter_grade(73) == "C")
# print(get_letter_grade(3) == "F" )
# print(get_letter_grade(-566))

def fizz_buzz(n):


	if (n % 3 == 0) and (n % 5 == 0):
		return "FizzBuzz"
	if n % 3 == 0:
		return "Fizz"
	if n % 5 == 0:
		return "Buzz"
	
	return n

assert fizz_buzz(3) == "Fizz"
assert fizz_buzz(5) == "Buzz"
assert fizz_buzz(15) == "FizzBuzz"
assert fizz_buzz(7) == 7






