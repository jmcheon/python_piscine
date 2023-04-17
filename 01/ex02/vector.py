
class Vector:
	"""
		• values: list of list of floats (for row vector) or list of lists of single float (for column vector).
		• shape: tuple of 2 integers: (1,n) for a row vector of dimension n or (n,1) for a column vector of dimension n.
	"""
	def __init__(self, data):
		self.values = []
		# when data is a list
		if isinstance(data, list):
			# initialize a list of a list of floats : Vector([[0.0, 1.0, 2.0, 3.0]])
			if len(data) == 1 and isinstance(data[0], list) and len(data[0]) > 0 and all(isinstance(i, float) for i in data[0]):	
				self.values = data
				self.shape = (1, len(data[0]))
			# initialize a list of lists of single float : Vector([[0.0], [1.0], [2.0], [3.0]])
			elif all(isinstance(elem, list) and len(elem) == 1 and all(isinstance(i, float) for i in elem) for elem in data):
				self.values = data
				self.shape = (len(data), 1)
			else:
				raise ValueError("Invalid form of list,", data)

		# when data is a size
		elif isinstance(data, int):
			if data <= 0:
				raise ValueError("Size must be a positive integer")
			self.values = [[float(i)] for i in range(data)]
			self.shape = (data, 1)

		# when data is a tuple
		elif isinstance(data, tuple) and len(data) == 2 and all(isinstance(elem, int) and elem >= 0 for elem in data):
			if data[0] > data[1]:
				raise ValueError("First value of tuple must be greater than the second one")
			self.values = [[float(i)] for i in range(data[0], data[1])]
			self.shape = (data[1] - data[0], 1)
		else:
			raise ValueError("Invalid form of data,", data)

	def dot(self, other):
		if not isinstance(other, Vector):
			raise TypeError("Invalid input: dot product requires a Vector object.")
		if self.shape[1] != other.shape[0]:
			raise TypeError("Invalid input: dot product requires a Vector of compatible shape.")
		result = 0.0
		for i in range(self.shape[0]):
			for j in range(self.shape[1]):
				result += self.values[i][j] * other.values[j][i]
		return result

	def T(self):
		transposed = []
		for j in range(self.shape[1]):
			row = []
			for i in range(self.shape[0]):
				row.append(self.values[i][j])
			transposed.append(row)
		return Vector(transposed)

	# add & radd : only vectors of same shape.
	def __add__(self, other):
		if not isinstance(other, Vector):
			raise TypeError("Invalid input: dot product requires a Vector object.")
		if self.shape != other.shape:
			raise TypeError("Invalid input: dot product requires a Vector of same shape.")
		result = []
		for i in range(self.shape[0]):
			row = []
			for j in range(self.shape[1]):
				row.append(self.values[i][j] + other.values[i][j])
			result.append(row)
		return Vector(result)
	
	def __radd__(self, other):
		return other + self

	# sub & rsub: only vectors of same shape.
	def __sub__(self, other):
		if not isinstance(other, Vector):
			raise TypeError("Invalid input: dot product requires a Vector object.")
		if self.shape != other.shape:
			raise TypeError("Invalid input: dot product requires a Vector of same shape.")
		result = []
		for i in range(self.shape[0]):
			row = []
			for j in range(self.shape[1]):
				row.append(self.values[i][j] - other.values[i][j])
			result.append(row)
		return Vector(result)
	
	def __rsub__(self, other):
		return other - self

	# truediv : only with scalars (to perform division of Vector by a scalar).
	def __truediv__(self, scalar):
		if isinstance(scalar, Vector):
			raise NotImplementedError("Division with a Vector object is not implemented.")
		if not any(isinstance(scalar, scalar_type) for scalar_type in [int, float, complex]):
			raise TypeError("Invalid type of scalar value.")
		if scalar == 0:
			raise ValueError("Can't not divide by 0.")
		result = []
		for i in range(self.shape[0]):
			row = []
			for j in range(self.shape[1]):
				row.append(self.values[i][j] / scalar)
			result.append(row)
		return Vector(result)

	# rtruediv : raises an NotImplementedError with the message "Division of a scalar by a Vector is not defined here."
	def __rtruediv__(self, scalar):
		raise NotImplementedError("Division of a scalar by a Vector is not defined here.")

	# mul & rmul: only scalars (to perform multiplication of Vector by a scalar).
	def __mul__(self, scalar):
		if isinstance(scalar, Vector):
			raise NotImplementedError("Multiplication with a Vector object is not implemented.")
		if not any(isinstance(scalar, scalar_type) for scalar_type in [int, float, complex]):
			raise TypeError("Invalid type of scalar value.")
		result = []
		for i in range(self.shape[0]):
			row = []
			for j in range(self.shape[1]):
				row.append(self.values[i][j] * scalar)
			result.append(row)
		return Vector(result)

	def __rmul__(self, scalar):
		return self * scalar

	# must be identical, i.e we expect that print(vector) and vector within python interpretor behave the same, see correspond
	def __str__(self):
		txt = "{} {}".format(self.values, self.shape)
		return txt

	def __repr__(self):
		txt = "{} {}".format(self.values, self.shape)
		return txt
