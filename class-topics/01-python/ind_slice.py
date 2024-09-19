str_ = "Hello World"

print(str_[0])
print(str_[3])
# print(str_[1000000])

print(str_[-1])
print(str_[-3])

print(len(str_))
# print(str_[11])
print(str_[len(str_) - 1])
print(str_[len(str_) - 3])

print(str_[0:5])
print(str_[0:100000000])

print(str_[:5])
print(str_[6:])


print(str_[0:11:2])

print("tacocat"[::-1])

def is_palindrome(str_):
 return str_[::-1] == str_

print(is_palindrome("tacocat"))
print(is_palindrome("racecar"))
print(is_palindrome("hello"))