import numpy as np

class NumPyCreator:
	"""
	from_list(self, lst), from_tuple(self, tpl), from_iterable(self, itr), from_shape(self, shape, value), random(self, shape), identity(self, n)
	"""
	def from_list(self, lst):
		"""takes a list or nested lists and returns its corresponding Numpy array."""
		if not isinstance(lst, list):
			return None
		# invalid shape
		if not all(len(sublist) == len(lst[0]) for sublist in lst):
			return None
		return np.array(lst)

	def from_tuple(self, tpl):
		"""takes a tuple or nested tuples and returns its corresponding Numpy array."""
		if not isinstance(tpl, tuple):
			return None
		# invalid shape
		if not all(len(subtuple) == len(tpl[0]) for subtuple in tpl):
			return None
		return np.array(tpl)

	def from_iterable(self, itr):
		"""takes an iterable and returns an array which contains all its elements."""
		return np.array(list(itr))

	def from_shape(self, shape, value):
		"""
		returns an array filled with the same value.
		The first argument is a tuple which specifies the shape of the array, and the second
		argument specifies the value of the elements. This value must be 0 by default.
		"""
		return np.array(tpl)

	def random(self, shape):
		"""
		returns an array filled with random values. It takes as an
		argument a tuple which specifies the shape of the array.
		"""
		return np.array(tpl)

	def identity(self, n):
		"""returns an array representing the identity matrix of size n"""
		return np.array(tpl)


if __name__ == "__main__":
	npc = NumPyCreator()
	print(npc.from_list([[1,2,3],[6,3,4]]))
	print(npc.from_list([[1,2,3],[6,4]]))
	print(npc.from_list([[1,2,3],['a','b','c'],[6,4,7]]))
	print(npc.from_list(((1,2),(3,4))))
	print(npc.from_tuple(("a", "b", "c")))
	print(npc.from_tuple(["a", "b", "c"]))
	print(npc.from_iterable(range(5)))
	print(npc.from_shape(shape))
	print(npc.random(shape))
	print(npc.identity(4))
