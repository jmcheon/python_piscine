import numpy as np
from ImageProcessor import ImageProcessor
from PIL import Image



class ColorFilter:
	"""
	invert ,to_blue, to_green, to_red, to_celluloid(array), to_grayscale
	"""

	def __init__(self) -> None:
		pass

	def invert(self, array):
		"""

		◦ Authorized functions: .copy.
		◦ Authorized operators: +,-,=.

		Inverts the color of the image received as a numpy array.
		Args:
		-----
		array: numpy.ndarray corresponding to the image.
		Return:
		-------
		array: numpy.ndarray corresponding to the transformed image.
		None: otherwise.
		Raises:
		-------
		This function should not raise any Exception.
		"""
		if not isinstance(array, np.ndarray):
			return None
		inverted_array = np.copy(array)
		# to invert only RGB channels
		inverted_array[:, :, :3] = 1 - inverted_array[:, :, :3]
		return inverted_array

	def to_blue(self, array):
		"""
		
		◦ Authorized functions: .copy, .zeros,.shape,.dstack.
		◦ Authorized operators: =.

		Applies a blue filter to the image received as a numpy array.
		Args:
		-----
		array: numpy.ndarray corresponding to the image.
		Return:
		-------
		array: numpy.ndarray corresponding to the transformed image.
		None: otherwise.
		Raises:
		-------
		This function should not raise any Exception.
		"""
		if not isinstance(array, np.ndarray):
			return None
		# create an array of zeros with the same shape of the original array
		filtered_array = np.zeros(array.shape)
		# copy only BA from RGBA
		filtered_array[:, :, 2:] = np.copy(array[:, :, 2:])
		return filtered_array

	def to_green(self, array):
		"""

		◦ Authorized functions: .copy.
		◦ Authorized operators: *, =.

		Applies a green filter to the image received as a numpy array.
		Args:
		-----
		array: numpy.ndarray corresponding to the image.
		Return:
		-------
		array: numpy.ndarray corresponding to the transformed image.
		None: otherwise.
		Raises:
		-------
		This function should not raise any Exception.
		"""
		if not isinstance(array, np.ndarray):
			return None
		filtered_array = np.copy(array)
		# copy only GA from RGBA
		filtered_array[..., : 3:2] = np.copy(array[..., : 3:2]) * 0
		return filtered_array

	def to_red(self, array):
		"""

		◦ Authorized functions: .copy, .to_green,.to_blue.
		◦ Authorized operators: -,+, =.

		Applies a red filter to the image received as a numpy array.
		Args:
		-----
		array: numpy.ndarray corresponding to the image.
		Return:
		-------
		array: numpy.ndarray corresponding to the transformed image.
		None: otherwise.
		Raises:
		-------
		This function should not raise any Exception.
		"""
	def to_celluloid(self, array):
		"""

		◦ Authorized functions: .copy, .arange,.linspace, .min, .max.
		◦ Authorized operators: =, <=, >, & (or and).

		Applies a celluloid filter to the image received as a numpy array.
		Celluloid filter must display at least four thresholds of shades.
		Be careful! You are not asked to apply black contour on the object,
		you only have to work on the shades of your images.
		Remarks:
		celluloid filter is also known as cel-shading or toon-shading.
		Args:
		-----
		array: numpy.ndarray corresponding to the image.
		Return:
		-------
		array: numpy.ndarray corresponding to the transformed image.
		None: otherwise.
		Raises:
		-------
		This function should not raise any Exception.
		"""
	def to_grayscale(self, array, filter, **kwargs):
		"""

		◦ Authorized functions: .sum,.shape,.reshape,.broadcast_to,.as_type.
		◦ Authorized operators: *,/, =.
		
		Applies a grayscale filter to the image received as a numpy array.
		For filter = ’mean’/’m’: performs the mean of RBG channels.
		For filter = ’weight’/’w’: performs a weighted mean of RBG channels.
		Args:
		-----
		array: numpy.ndarray corresponding to the image.
		filter: string with accepted values in [’m’,’mean’,’w’,’weight’]
		weights: [kwargs] list of 3 floats where the sum equals to 1,
		corresponding to the weights of each RBG channels.
		Return:
		-------
		array: numpy.ndarray corresponding to the transformed image.
		None: otherwise.
		Raises:
		-------
		This function should not raise any Exception.
		"""

if __name__ == "__main__":
	imp = ImageProcessor()
	#arr = imp.load("./42AI.png")
	arr = imp.load("./elon_canaGAN.png")
	#image = Image.open("./elon_canaGAN.png")
	#print(image.mode)
	#with np.printoptions(threshold=np.inf):
	#	print(arr)
	#print("\n=====================================\n")
	cf = ColorFilter()
	#arr = cf.invert(arr)
	#print(arr)
	imp.display(arr)
	#arr = cf.to_blue(arr)
	arr = cf.to_green(arr)
	imp.display(arr)
