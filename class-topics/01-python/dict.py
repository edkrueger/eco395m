my_dict = {
    "dog": "man's best friend",
    "cat": "a small animal",
}

print(my_dict["dog"])
# print(my_dict["mouse"])
print(my_dict.get("mouse"))
print(my_dict.get("dog"))

my_dict["mouse"] = "a small rodent"

print(my_dict)

my_dict["mouse"] = "a very small rodent"

print(my_dict)

del my_dict["mouse"]

print(my_dict)

print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

# for e in my_dict:
#     print(f"key={e}, value={my_dict[e]}")

# for t in my_dict.items():
#     print(f"key={t[0]}, value={t[1]}")

for k, v in my_dict.items():
    print(f"key={k}, value={v}")

def merge_dicts(dict_a, dict_b):

    out_dict = {}

    for k, v in dict_a.items():
        out_dict[k] = v

    for k, v in dict_b.items():
        out_dict[k] = v
    
    return out_dict

my_dict_b = {
    "fish": "a swimming animal",
    "bird": "a flying animal"
}

print(merge_dicts(my_dict, my_dict_b))
print(my_dict)
print(my_dict_b)

print({**my_dict, **my_dict_b})

# realistic representation of dictionary book

my_realistic_dict = {
    "dog": [
        "man's best friend",
        "a small animal"
    ],
    "cat": [
        "a small animal",
        "man's awkward roommate"
    ]
}

print(my_realistic_dict)

# def count_the_numbers(my_list):

#     count = {}

#     for e in my_list:
#         if not e in count:
#             count[e] = 1
#         else:
#             count[e] += 1
    
#     return count

# def char_freq(my_list):

#     count = {}

#     for char in my_list:

#         char_lower = char.lower()

#         if not char_lower in count:
#             count[char_lower] = 1
#         else:
#             count[char_lower] += 1
    
#     return count

# print(count_the_numbers([1, 9, 2, 3, 4, 9, 9]))

# english_statement = """First, I wake up. Then, I get dressed. I walk to school. I do not ride a bike. I do not ride the bus. I like to go to school. It rains. I do not like rain. I eat lunch. I eat a sandwich and an apple."""
# print(char_freq(english_statement))





