import os

print(os.listdir("."))
print(os.listdir(".."))
print(os.listdir("data/"))

os.makedirs("artifacts", exist_ok=True)

with open("hello.txt", "w+") as f:
    f.write("hello\n")
    f.write("world\\n\n")
    f.write("another line\n")
    f.writelines(["1\n", "2\n", "3\n", "4\n", "5\n"])

with open("hello.txt", "r") as f:

    line = f.readline().strip()

    print(line)
    
    # line2 = f.readline()
    # print(line2)
    # print(f.read())
    # print(f.readlines())

    for line in f:
        print(line)
