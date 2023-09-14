d = {"hello": "a greeting of welcome", "world": "a planet"}
d1 = {"world": "a planet", "hello": "a greeting of welcome"}
d2 = {"world": "a planet", "hello": "a greeting of welcome", 0: 5}

# print(d)
# print(d1)
# print(d == d1)

# # print(d[0])
# print(d2[0])
# print(d["hello"])

# print(d.get(123))

# print(d)
# d["python"] = "a programming language"
# print(d)
# d["python"] = "a snake"
# print(d)

# realistic_dict = {
#     "hello": ["a greeting of welcome", "the first thing we say in a programming language"],
#     "world": ["a planet"],
#     "python": ["a snake"]
# }

# print(realistic_dict)
# print(realistic_dict["hello"])
# print(type(realistic_dict["hello"]))

# realistic_dict["python"].append("a programming language")
# print(realistic_dict)
# realistic_dict["python"] = realistic_dict["python"] + ["a member of Monty Python"]
# print(realistic_dict)

# print(list(realistic_dict.keys()))
# print(list(realistic_dict.values()))
# print(list(realistic_dict.items()))
# print(list(d2.items()))

for e in d2:
    print(e)

# for e in d2.keys():
#     print(e)

# for e in d2.values():
#     print(e)

# for e in d2.keys():
#     print(f"key={e}, value={d2[e]}")

# for e in d2.items():
#     print(f"key={e[0]}, value={e[1]}")

# for k, v in d2.items():
#     print(f"key={k}, value={v}")

print(0 in d2.keys())
print(0 in d2)
print(5 in d2)
print(5 in d2.values())


a = {1:2, 3:4, 5:6}
b = {2:3, 4:5, 6:7, 1:3}

def merge_dicts(d1, d2):

    d = {}

    for k, v in d1.items():
        d[k] = v

    for k, v in d2.items():
        d[k] = v

    return d

print(merge_dicts(a, b))
print(merge_dicts(b, a))
print({**a, **b})
print({**b, **a})

def count_char_count(str_):

    dict_ = {}

    for char_ in str_:
        if char_ in dict_:
            dict_[char_] = dict_[char_] + 1
        else:
            dict_[char_] = 1

    return dict_


def count_char_freq(str_):

    dict_ = count_char_count(str_)

    len_ = len(str_)

    freq_dict = {}

    for char_, count in dict_.items():
        freq_dict[char_] = count / len_
    
    return freq_dict

def count_char_freq2(str_):

    dict_ = count_char_count(str_)

    len_ = len(str_)

    return {char_: count / len_ for char_, count in dict_.items()}

print(count_char_count("abba"))
print(count_char_freq("abba"))
print(count_char_freq2("abba"))




