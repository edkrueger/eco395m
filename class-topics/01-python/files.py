import os

PATH = os.path.join("data", "lines.txt")
OUT_PATH = os.path.join("artifact.txt")


print(PATH)

with open(PATH) as file:
    print(file.read())


with open(PATH) as file:
    print(file.readline())
    print(file.readline())
    print(file.readline())
    print(file.readline())
    print(file.readline())
    print(file.readline())
    print(file.readline())
    print(file.readline())

with open(PATH) as file:
    print(file.readlines())

# skip the first line, print the rest
with open(PATH) as file:
    file.readline()
    print(file.read())

with open(PATH) as file:

    lines = []

    for line in file:
        lines.append(line.strip())

    print(lines)

data = [
    1,2,3,4,5,6,7,8,3,5,7,8,3,2
]

with open(OUT_PATH, mode="w+") as out_file:
    for d in data:
        out_file.write(str(d) + "\n")