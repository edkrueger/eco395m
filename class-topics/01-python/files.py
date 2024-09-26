import os

IN_PATH = os.path.join("data", "lines.txt")
OUT_PATH = os.path.join("data", "outfile.txt")
OUT_PATH_2 = os.path.join("data", "outfile2.txt")

with open(IN_PATH, "r") as file:
    for line in file:
        print(line)

data = list(range(10))

print(data)

with open(OUT_PATH, "w+") as outfile:
    for d in data:
        outfile.write(str(d))
        outfile.write("\n")

with open(OUT_PATH_2, "w+") as outfile2:
    outfile2.writelines([str(d) + "\n" for d in data])



    

