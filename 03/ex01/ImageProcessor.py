import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread


class ImageProcessor:
	"""
		load(path), display(array)
	"""
	def __init__(self) -> None:
		pass

	def load(self, path):
		"""
		it opens the PNG file specified by the path argument and returns an
		array with the RGB values of the pixels image. It must display a message specifying
		the dimensions of the image (e.g. 340 x 500).
		"""
		try:
			image = imread(path)
			print("Loading image of dimensions", image.shape[0], "X", image.shape[1])
			return image
		except Exception as e:
			print(f"Exception: {e.__class__.__name__} -- strerror: {e}")
			return None

	def display(self, array):
		"""
		it takes a numpy array as an argument and displays the corresponding RGB image.
		"""
		plt.figure("loaded image")
		plt.axis("off")
		plt.imshow(array)
		plt.show()

if __name__ == "__main__":
	imp = ImageProcessor()
	arr = imp.load("non_existing_file.png")
	print(arr)
	arr = imp.load("empty_file.png")
	print(arr)
	arr = imp.load("./42AI.png")
	print(arr)
	imp.display(arr)
