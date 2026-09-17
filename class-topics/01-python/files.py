file = open("newfile.txt", "w+")
file.write("hello\n")
file.write("world\n")
file.close()

with open("newfile.txt", "w+") as file:
	file.write("hello\n")
	file.write("world\n")

with open("newfile.txt", "a+") as file:
	file.write("hello\n")
	file.write("world\n")

with open("newfile.txt", "r") as file:
	# for line in file:
	# 	print(line)

	# for line in file:
	# 	print(line)

	print(list(file))