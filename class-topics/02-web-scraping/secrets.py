import os

from dotenv import load_dotenv

load_dotenv()

SECRET = os.environ["SECRET"]

# shouldn't do this in pratice
print(SECRET)