# import pprint
from pprint import pprint

d1 = {
	"goose": ["a type of bird"],
	"mouse": ["a type of rodent"],
	"car": ["a vehicle"],
	"dog": ["a mammal", "man's best friend"],
	"python": ["a snake", "a programming language"],
	"million": 100000
}

# pprint.pprint(d1)
pprint(d1, indent=4, underscore_numbers=True)