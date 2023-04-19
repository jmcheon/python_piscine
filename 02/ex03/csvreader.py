import sys

class CsvReader():
	def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
		self.filename = filename
		self.sep = sep
		self.header = header
		self.skip_top = skip_top
		self.skip_bottom = skip_bottom
		self.data = []
		self.file = None

	def __enter__(self):
		try:
			self.file = open(self.filename, 'r')
		except FileNotFoundError:
			return None
		for line in self.file:
			self.data.append(list(map(str.strip, line.split(self.sep))))
		if all(len(elem) == len(self.data[0]) for elem in self.data):
			return self
		return None


	def __exit__(self, exc_type, exc_val, traceback):
		if self.file:
			self.file.close()

	def getdata(self):
		""" Retrieves the data/records from skip_top to skip bottom.
		Return:
		nested list (list(list, list, ...)) representing the data.
		"""
		# ... Your code here ...
		start = self.skip_top
		end = len(self.data) - self.skip_bottom
		if self.header:
			return self.data[start + 1:end]
		return self.data[start:end]

	def getheader(self):
		""" Retrieves the header from csv file.
		Returns:
		list: representing the data (when self.header is True).
		None: (when self.header is False).
		"""
		# ... Your code here ...
		if self.header:
			return self.data[0]
		return None 


if __name__ == "__main__":
#	with CsvReader('good.csv') as f:
#		data = f.getdata()
#		header = f.getheader()
#	
#	with CsvReader('bad.csv') as f:
#		if f == None:
#			print("File is corrupted")

	filename = sys.argv[1]
	with CsvReader(filename, skip_top=18, skip_bottom=0) as reader:
		if reader == None:
			print("File is corrupted or missing")
		else:
			print(reader.getheader(), end = "\n")
			print(reader.getdata(), end = "\n\n")
	
	with CsvReader(filename, header = True, skip_top=17, skip_bottom=0) as reader:
		if reader == None:
			print("File is corrupted or missing")
		else:
			print(reader.getheader(), end = "\n")
			print(reader.getdata(), end = "\n\n")
