str_ = "Hello World"

str_cap = str_.upper()

print(str_cap)
print(str_)

str_0 = str_

# not a great coding pratice
str_ = 2 * str_

print(str_)
print(str_0)

print(id(str_))
print(id(str_0))

print(str_.upper())
print(str_.lower())
print(str_.title())
print(str_.swapcase())

print(str_.title().swapcase())
