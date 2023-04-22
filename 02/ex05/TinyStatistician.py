class TinyStatistician:
	"""
		• mean(x), median(x), quartiles(x), var(x), std(x)
	"""
	def mean(self, x):
		if not isinstance(x, list) or len(x) == 0:
			return None
		result = 0.0
		for elem in x:
			result += elem
		return result / len(x)

	def median(self, x):
		if not isinstance(x, list) or len(x) == 0:
			return None
		numbers = sorted(x)
		middle = len(numbers) // 2
	#	print("==============median()===============")
	#	print("sorted list:", numbers) 
	#	print("len(lst) / 2 = ", len(numbers) / 2)
	#	print("middle index:", middle)
	#	print("=====================================\n")
		if len(numbers) % 2 == 0:
			return float(numbers[middle - 1])
		else:
			return float(numbers[middle])

	def quartiles(self, x):
		if not isinstance(x, list) or len(x) == 0:
			return None
		numbers = sorted(x)
		n = len(x)
		# q1 > 1/4 * n
		q1 = self.median(numbers[:(n + 1)//2])
		# q3 > 2/4 * n
		q3 = self.median(numbers[(n + 1)//2:])
		return [q1, q3]

	def var(self, x):
		if not isinstance(x, list) or len(x) == 0:
			return None
		mean = self.mean(x)
		suqared_diff_sum = 0
		for num in x:
			suqared_diff_sum += (num - mean) ** 2
		return suqared_diff_sum / len(x)

	def std(self, x):
		if not isinstance(x, list) or len(x) == 0:
			return None
		return self.var(x) ** 0.5

def ex1(t):
	a = [1, 42, 300, 10, 59]
	#a = [] 
	print(t.mean(a)) # 82.4
	print(t.median(a)) # 42
	print(t.quartiles(a)) # 10 59
	print(t.var(a)) # 12279.439999999999
	print(t.std(a)) # 110.81263465868862

def ex2(t):
	lst = [14, 17, 10, 14, 18, 20, 13]
	print(t.mean(lst)) # 
	print(t.median(lst)) # 14
	print(t.quartiles(lst)) # 13, 18
	print(t.var(lst)) # 
	print(t.std(lst)) # 

def ex3(t):
	lst2 = [177, 180, 175, 182, 190, 169, 185, 191, 193]
	print(t.mean(lst2)) # 
	print(t.median(lst2)) # 182
	print(t.quartiles(lst2)) # 177 190
	print(t.var(lst2)) # 
	print(t.std(lst2)) # 

if __name__ == "__main__":
	t = TinyStatistician()
	ex1(t)
