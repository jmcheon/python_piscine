from collections.abc import Iterable

def ft_filter(function_to_apply, iterable):
	"""
	Filter the result of function apply to all elements of the iterable.
	Args:
	function_to_apply: a function taking an iterable.
	iterable: an iterable object (list, tuple, iterator).
	Return:
	An iterable.
	None if the iterable can not be used by the function.
	"""
	if not (isinstance(iterable, Iterable) or iterable):
		raise TypeError("Invalid input: second argument should be an iterable argument")

	for elem in iterable:
		if function_to_apply(elem):
			yield (elem)

