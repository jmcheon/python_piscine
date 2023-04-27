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
		if array.shape[-1] == 4:
			# RGBA image[top:bottom, left:right, red:green:blue:alpha]
			inverted_array[:, :, :3] = 1 - inverted_array[:, :, :3]
		else:
			# RGB image[top:bottom, left:right, red:green:blue]
			inverted_array[:, :, :] = 1 - inverted_array[:, :, :]
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
		filtered_array[..., [0, 2]] = np.copy(array[..., [0, 2]]) * 0
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
		if not isinstance(array, np.ndarray):
			return None
		image = np.copy(array)
		filtered_array = image - (self.to_blue(image) + self.to_green(image))
		if array.shape[-1] == 4:
			filtered_array[..., [3]] = image[..., [3]]
		return filtered_array

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
		if not isinstance(array, np.ndarray):
			return None
		image = np.copy(array)
		thresholds = np.linspace(0.0, 1.0, 4)
		for shade in thresholds:
			image[array >= shade] = shade
		return image

	def to_grayscale(self, array, filter, **kwargs):
		"""

		◦ Authorized functions: .sum,.shape,.reshape,.broadcast_to,.as_type.
		◦ Authorized operators: *,/, =.
		
		Applies a grayscale filter to the image received as a numpy array.
		For filter = 'mean'/'m': performs the mean of RBG channels.
		For filter = 'weight'/'w': performs a weighted mean of RBG channels.
		Args:
		-----
		array: numpy.ndarray corresponding to the image.
		filter: string with accepted values in ['m','mean','w','weight']
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
		if not isinstance(array, np.ndarray):
			return None
		if filter in ['m', 'mean']:
			image = np.copy(array)
			# to express only height, width from height, width, channels
			gray_vals = image[...,:3].sum(axis=-1) / image[...,:3].shape[-1]
			filtered_array = np.broadcast_to(gray_vals[..., np.newaxis], image.shape)
			image = np.copy(filtered_array)
			if array.shape[-1] == 4:
				image[..., [3]] = array[..., [3]]
			return image 
		elif filter in ['w', 'weight']:
			image = np.copy(array)
			weight = np.array(kwargs["weights"])
			gray_vals = (image[...,:3] * weight).sum(axis=-1)
			filtered_array = np.broadcast_to(gray_vals[..., np.newaxis], image.shape)
			image = np.copy(filtered_array)
			if array.shape[-1] == 4:
				image[..., [3]] = array[..., [3]]
			return image
		else:
			return None

def ex1():
	#image = Image.open("./42AI.png")
	#print(image.mode)
	arr = imp.load("./42AI.png")
	for f in [cf.to_red, cf.to_green, cf.to_blue, cf.invert, cf.to_celluloid]:
		imp.display(f(arr))

	im = cf.to_grayscale(arr, "m")
	imp.display(im)
	#with np.printoptions(threshold=np.inf):
	#	print(im[190, 190])
	
	im = cf.to_grayscale(arr, "w", weights = [0.2126, 0.7152, 0.0722])
	imp.display(im)
	#with np.printoptions(threshold=np.inf):
	#	print(im[190, 190])

def ex2():
	#image = Image.open("./elon_canaGAN.png")
	#print(image.mode)
	arr = imp.load("./elon_canaGAN.png")
	for f in [cf.to_red, cf.to_green, cf.to_blue, cf.invert, cf.to_celluloid]:
		imp.display(f(arr))

	im = cf.to_grayscale(arr, "m")
	imp.display(im)
	#with np.printoptions(threshold=np.inf):
	#	print(im[190, 190])
	
	im = cf.to_grayscale(arr, "w", weights = [0.2126, 0.7152, 0.0722])
	imp.display(im)
	#with np.printoptions(threshold=np.inf):
	#	print(im[190, 190])

if __name__ == "__main__":
	imp = ImageProcessor()
	cf = ColorFilter()
	ex2()
