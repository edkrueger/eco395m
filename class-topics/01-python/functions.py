# fruitless
def say_hello():
	print("Hello")

# fruitful function
def add(x, y):
	return x + y

# say_hello()
# add(1, 2)

say_hello_result = say_hello()
add_result = add(1, 2)

print(say_hello_result)
print(add_result)

print(bool(None))

print(add("Hello", "World"))

# TypeError
# print(add(1, "World"))
# print(add("World", 1))