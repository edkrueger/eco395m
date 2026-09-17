d0 = {
	1: 123,
	0: 456
}

d1 = {
	"goose": "a type of bird",
	"mouse": "a type of rodent",
	"car": "a vehicle"
}

# print(d1)
# print(d1["car"])

# # print(d1[0])
# print(d0[0])

# d1["cat"] = "A type of mammal"
# print(d1)
# d1["dog"] = "Man's best friend."
# print(d1)
# d1["dog"] = "Man's best friend, a type of mammal"
# print(d1)

# # print(d1["bird"])
# print(d1.get("bird"))
# print(d1.get("dog"))

# print(d1.get("bird", "default"))
# print(d1.get("dog", "default"))

print(d1.keys())
print(d1.values())
print(list(d1.items()))

# for k in d1.keys():
# 	v = d1[k]
# 	print(f"{k=} {v=}")

for t in d1.items():
	k = t[0]
	v = t[1]
	print(f"{k=} {v=}")

a, b = ("hello", "world")
print(a)
print(b)

for k, v in d1.items():
	print(f"{k=} {v=}")


