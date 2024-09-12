list_ = [0, 1.3, 5j, "asdf", ["jel"], True]

print(list_[0])
print(list_[3])
# print(list_[1000000])

print(list_[-1])
print(list_[-3])

print(len(list_))
# print(list_[11])
print(list_[len(list_) - 1])
print(list_[len(list_) - 3])

print(list_[0:5])
print(list_[0:100000000])

print(list_[:5])
print(list_[6:])


print(list_[0:11:2])

print(list_[::-1])

print(list_[4][0][1])