import pandas as pd

class FileLoader:
	"""
	load(self, path), display(self, df, n)
	"""

	def __init__(self) -> None:
		pass

	def load(self, path):
		"""
		it takes as an argument the file path of the dataset to load,
		displays a message specifying the dimensions of the dataset (e.g. 340 x 500) and
		returns the dataset loaded as a pandas.DataFrame.
		"""
		df = pd.read_csv(path)
		print("Loading dataset of dimensions", len(df.index), "x", len(df.columns))
		return df

	def display(self, df, n):
		"""
		it takes a pandas.DataFrame and an integer as arguments,
		displays the first n rows of the dataset if n is positive, or the last n rows if n is
		negative.
		"""
		if n > 0:
			print(df.head(n))
		else:
			print(df.tail(abs(n)))

if __name__ == "__main__":
	loader = FileLoader()
	data = loader.load("../athlete_events.csv")
	loader.display(data, 12)
	#loader.display(data, -42)
