def is_even_say_hello_ow_goodbye(x):
	"""
	Say "hello" if x is even.
	"""

	if x % 2 == 0:
		print("hello")
	else:
		print("goodbye")
	return

# print(is_even_say_hello_ow_goodbye.__doc__)

# is_even_say_hello_ow_goodbye(1)
# is_even_say_hello_ow_goodbye(2)

# def is_even(x):
# 	"""
# 	Return True if x is even.
# 	ow return False
# 	"""

# 	if x % 2 == 0:
# 		return True
# 	else:
# 		return False

def is_even(x):
	"""
	Return True if x is even.
	ow return False
	"""

	return x % 2 == 0

# print(is_even(0))
# print(is_even(2))
# print(is_even(1))

# def grade(x):

# 	"""
# 	Takes a numerical grade x,
# 	and converts its to a letter grade,
# 	"A", "B", ..., "F"
# 	"""

# 	your_grade = None

# 	if x >= 90:
# 		your_grade = "A"
# 	elif x >= 80:
# 		your_grade = "B"
# 	elif x >= 70:
# 		your_grade = "C"
# 	elif x >= 60:
# 		your_grade = "D"
# 	else:
# 		your_grade = "F"

# 	return your_grade

# def grade(x):

# 	"""
# 	Takes a numerical grade x,
# 	and converts its to a letter grade,
# 	"A", "B", ..., "F"
# 	"""

# 	if x >= 90:
# 		return "A"
# 	if 80 <= x < 90:
# 		return "B"
# 	if 70 <= x < 80:
# 		return "C"
# 	if 60 <= x < 70:
# 		return "D"
	
# 	return "F"

# print(grade(50))
# print(grade(60))
# print(grade(70))
# print(grade(100))

def fizzbuzz_condition_return(x):
	"""
	If a number is divisible 3 return fizz
	If a number is divisible 5 return buzz
	and if a number is divisible by both return fizzbuzz instead
	"""

	if (x % 3 == 0) and (x % 5 == 0):
		return "fizzbuzz"

	if x % 3 == 0:
		return "fizz"
		
	if x % 5 == 0:
		return "buzz"


print(fizzbuzz_condition_return(15))
