import string
import sys

def text_analyzer(s = None):
	"""
	This function counts the number of upper characters, lower characters,
	punctuation and spaces in a given text.
	"""
	if s is None:
		s = input("What is the text to analyze?\n>> ")
	if not isinstance(s, str):
		print("AssertionError: argument is not a string")
		return None
	uppercase_count = 0
	lowercase_count = 0
	punctuation_count = 0
	space_count = 0

	for c in s:
		if c.isupper():
			uppercase_count += 1
		elif c.islower():
			lowercase_count += 1
		elif c in string.punctuation:
			punctuation_count += 1
		elif c.isspace():
			space_count += 1
	print("The text contains", len(s), "character(s):")
	print("-", uppercase_count, "upper letter(s)")
	print("-", lowercase_count, "lower letter(s)")
	print("-", punctuation_count, "punctuation marks(s)")
	print("-", space_count, "space(s)")

if __name__ == "__main__":
	if len(sys.argv) == 1:
		print("Usage: python count.py <string>")
		print("Example:")
		print("\tpython count.py 'Hello World!'")
	elif len(sys.argv) == 2:
		text_analyzer(sys.argv[1])
	else:
		print("AssertionError: more than one argument are provided")
