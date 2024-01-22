my_string = "hello world"
str_upper = my_string.upper()

# the string's content uppercased
str_upper

# original string is not changed
my_string

"absFds".swapcase()

type(my_string.title())

# bad practice, demo that reassignment is not mutation
a = "abc"
print(a)
print(id(a))
a = a.upper()
print(a)
print(id(a))

# indexes
my_string[0]
my_string[len(my_string) - 1]
my_string[-1]

my_string[0:5]
my_string[:5]
my_string[6:11]
my_string[6:-1]
my_string[6:]
my_string[6:-2]

my_string[0:5]
my_string[0:5:1]
my_string[-1:0:-1]
my_string[::-1]

def is_palindrome(str_):
    return str_ == str_[::-1]

print(is_palindrome("tacocat"))
print(is_palindrome("hello"))