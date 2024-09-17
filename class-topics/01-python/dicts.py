import pprint

dict_ = {
    "cat": "A furry mammal",
    "dog": ["A furry mammal", "man's best friend"],
    0: 8j,
    (1,2): "value",
    "dict": {},
}

pprint.pprint(dict_)
# print(dict_)

# print(dict_["cat"])
# print(dict_[0])
# print(dict_["dog"])

# dict_["mouse"] = ["A common house pest", "a pet"]
# print(dict_)
# dict_["cat"] = ["A common house pest", "a pet"]
# print(dict_)

# del dict_["dog"]
# print(dict_)

# # print(dict_["asdf"])
# r = dict_.get("asdf")
# print(r)
# r = dict_.get("cat")
# print(r)

# print("Hello World")

# print(dict_.keys())
# print(dict_.values())
# print(dict_.items())

# print(dict_)
# print("dog" in dict_)
# print("dog" in dict_.keys())

# grades = {
#     "Edward": 60,
#     "Sue": 100,
#     "Mary": 32,
# }

# for k in grades:
#     print(k)
#     v = grades[k]
#     print(v)
#     print(f"{k} and grade {v}")

# def count_chars(str_):

#     counts = {}

#     for char in str_:
#         if char in counts:
#             counts[char] = counts[char] + 1
#         else:
#             counts[char] = 1

#     return counts

# print(count_chars("hello world"))
