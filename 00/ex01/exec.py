import sys

def reverse_swap_case():
	s = ' '.join(sys.argv[1:])
	reversed_str = s[::-1]
	swaped_str = reversed_str.swapcase()
	return swaped_str
	

if len(sys.argv) != 1:
	#print(sys.argv[1:])
	reversed_swapped_str = reverse_swap_case()
	print(reversed_swapped_str)
