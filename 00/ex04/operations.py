import sys

def operations(A, B):
	try:
		A = int(A)
		B = int(B)
	except ValueError:
		print("AssertionError: only integers")
		return None
	print("Sum:       ", A+B)
	print("Difference:", A-B)
	print("Product:   ", A*B)
	if B == 0:
		print("Quotient:   ERROR (division by zero)")
		print("Remainder:  ERROR (modulo by zero)")
	else:
		print("Quotient:  ", A/B)
		print("Remainder: ", A%B)


if __name__ == "__main__":
	if len(sys.argv) == 1 or len(sys.argv) == 2:
		print("Usage: python operations.py <number1> <number2>")
		print("Example:")
		print("\tpython operations.py 10 3")
	elif len(sys.argv) == 3:
		operations(sys.argv[1], sys.argv[2])
	elif len(sys.argv) > 3:
		print("AssertionError: too many arguments")
