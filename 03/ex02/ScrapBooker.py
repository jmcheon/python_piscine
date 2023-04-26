import numpy as np
import sys

class ScrapBooker:
	"""
		crop, thin, juxtapose, mosaic.
	"""

	def __init__(self) -> None:
		pass

	def check_shape(self, tlp):
		if not isinstance(tlp, tuple) or len(tlp) != 2 or not all(isinstance(n, int) for n in tlp):
			return False
		if tlp[0] < 0 or tlp[1] < 0:
			return False
		return True

	def crop(self, array, dim, position=(0,0)):
		"""
		Crops the image as a rectangle via dim arguments (being the new height
		and width of the image) from the coordinates given by position arguments.
		Args:
		-----
		array: numpy.ndarray
		dim: tuple of 2 integers.
		position: tuple of 2 integers.
		Return:
		-------
		new_arr: the cropped numpy.ndarray.
		None (if combinaison of parameters not compatible).
		Raise:
		------
		This function should not raise any Exception.
		"""
		if not isinstance(array, np.ndarray) or not self.check_shape(dim) or not self.check_shape(position):
			return None
		pos_x = position[0]
		pos_y = position[1]
		dim_x = position[0] + dim[0]
		dim_y = position[1] + dim[1]
		if dim_x > len(array) or dim_y > len(array[0]):
			return None

		return array[pos_x:dim_x, pos_y:dim_y]

	def thin(self, array, n, axis):
		"""
		Deletes every n-th line pixels along the specified axis (0: Horizontal, 1: Vertical)
		Args:
		-----
		array: numpy.ndarray.
		n: non null positive integer lower than the number of row/column of the array
		(depending of axis value).
		axis: positive non null integer.
		Return:
		-------
		new_arr: thined numpy.ndarray.
		None (if combinaison of parameters not compatible).
		Raise:
		------
		This function should not raise any Exception.
		"""
		max_index = 0
		if not isinstance(array, np.ndarray) or not isinstance(n, int) or n <= 0 or axis not in [0, 1]:
			return None
		if axis == 1: 
			max_index = len(array)
			if n > len(array): 
				print("Invalid input: n should be lower then the number of column:", len(array))
				return None
		if axis == 0:
			max_index = len(array[0])
			if n > len(array[0]):
				print("Invalid input: n should be lower then the number of row:", len(array[0]))
				return None
		return np.delete(array, np.arange(n - 1, max_index, n), ~axis)

	def juxtapose(self, array, n, axis):
		"""
		Juxtaposes n copies of the image along the specified axis.
		Args:
		-----
		array: numpy.ndarray.
		n: positive non null integer.
		axis: integer of value 0 or 1.
		Return:
		-------
		new_arr: juxtaposed numpy.ndarray.
		None (combinaison of parameters not compatible).
		Raises:
		-------
		This function should not raise any Exception.
		"""
		if not isinstance(array, np.ndarray) or not isinstance(n, int) or n <= 0 or axis not in [0, 1]:
			return None
		if axis:
			return np.tile(array, (1, n))
		return np.tile(array, (n, 1))

	def mosaic(self, array, dim):
		"""
		Makes a grid with multiple copies of the array. The dim argument specifies
		the number of repetition along each dimensions.
		Args:
		-----
		array: numpy.ndarray.
		dim: tuple of 2 integers.
		Return:
		-------
		new_arr: mosaic numpy.ndarray.
		None (combinaison of parameters not compatible).
		Raises:
		-------
		This function should not raise any Exception.
		"""
		if not isinstance(array, np.ndarray) or not self.check_shape(dim):
			return None
		return np.tile(array, dim)

def basic_crop_test():
	print(arr1)
	print(spb.crop(arr1, (3,1),(1,0)))

	print(spb.crop(arr1, (3,-1),(1,0)))
	print(spb.crop(arr1, (3,1),(-1,0)))
	print(spb.crop(arr1, (3,1),(0)))
	print(spb.crop(arr1, (3,1),[1,0]))
	print(spb.crop(arr1, (3,1,2),(1,0)))
	print(spb.crop(arr1, (3,1.2),(1,0)))

def ex_crop():
	if len(sys.argv) != 5:
		print("Usage: python ScrapBooker.py [int(dim x)] [int(dim y)] [int(pos x)] [int(pos y)]")
		print("\tcrop(array, (dim x, dim y), (pos x, pos y))")
	else:
		dim = (int(sys.argv[1]), int(sys.argv[2]))
		pos = (int(sys.argv[3]), int(sys.argv[4]))
		print(arr1)
		print("dim:", dim, "pos:", pos)

		print(spb.crop(arr1, dim, pos))

def ex_thin():
	if len(sys.argv) != 3:
		print("Usage: python ScrapBooker.py [int(n)] [int(axis)]")
		print("\tthin(array, n, axis)")
	else:
		n = int(sys.argv[1])
		axis = int(sys.argv[2])
		print(arr2)
		print("n:", n, "axis:", axis)

		print(spb.thin(arr2, n, axis))

def ex_juxtapose():
	if len(sys.argv) != 3:
		print("Usage: python ScrapBooker.py [int(n)] [int(axis)]")
		print("\tjuxtapose(array, n, axis)")
	else:
		n = int(sys.argv[1])
		axis = int(sys.argv[2])
		print(arr3)
		print("n:", n, "axis:", axis)

		print(spb.juxtapose(arr3, n, axis))

def ex_mosaic():
	if len(sys.argv) != 3:
		print("Usage: python ScrapBooker.py [int(dim x)] [int(dim y)]")
		print("\tmosaic(array, (dim x, dim y))")
	else:
		dim = (int(sys.argv[1]), int(sys.argv[2]))
		print(arr3)
		print("dim:", dim)

		print(spb.mosaic(arr3, dim))
if __name__ == "__main__":
	spb = ScrapBooker()
	arr1 = np.arange(0,25).reshape(5,5)
	arr2 = np.array("A B C D E F G H I".split() * 6).reshape(-1,9)
	arr3 = np.array([[1, 2, 3],[1, 2, 3],[1, 2, 3]])
	#basic_crop_test():
	ex_crop()
	#ex_thin()
	#ex_juxtapose()
	#ex_mosaic()
