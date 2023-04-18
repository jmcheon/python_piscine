from collections.abc import Iterable

def ft_reduce(function_to_apply, iterable):
	"""
	Apply function of two arguments cumulatively.
	Args:
	function_to_apply: a function taking an iterable.
	iterable: an iterable object (list, tuple, iterator).
	Return:
	A value, of same type of elements in the iterable parameter.
	None if the iterable can not be used by the function.
	"""
	# ... Your code here ...
	if not (isinstance(iterable, Iterable) or iterable):
		raise TypeError("Invalid input: second argument should be an iterable argument")

	accumulator = iterable[0]
	for elem in iterable[1:]:
		accumulator = function_to_apply(accumulator, elem)
	return accumulator 
