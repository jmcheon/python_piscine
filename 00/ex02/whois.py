import sys

if len(sys.argv) == 1:
	print("Usage: python whois.py <number>")
	print("Example:")
	print("\tpython whois.py 1")
	sys.exit(0)

if len(sys.argv) != 2:
	print("AssertionError: more than one argument are provided")
	sys.exit(1)

try:
	num = int(sys.argv[1])
except ValueError:
	print("AssertionError: argument is not an integer")
	sys.exit(1)

if num == 0:
	print("I'm Zero.")
elif num % 2 == 0:
	print("I'm Even.")
else:
	print("I'm Odd.")

