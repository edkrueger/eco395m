import os

# os.mkdir("a_dir")

os.makedirs("a_dir", exist_ok=True)

path_ = os.path.join("hello", "world", "hello")
print(path_)
