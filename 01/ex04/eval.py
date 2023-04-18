
class Evaluator:

	@staticmethod
	def zip_evaluate(coefs, words):
		"""
		Compute the sum of the lengths of every words in a given list weighted by a list of coefficients using zip.
		
		Args:
		coefs (list): List of coefficients.
		words (list): List of words.
		
		Returns:
		int: Sum of the lengths of words weighted by coefficients, or -1 if the lists have different lengths.
		"""
		if not (isinstance(coefs, list)):
			return -1
		for coef in coefs:
			if not type(coef) in [int, float, complex]:
				return -1
		if not (isinstance(words, list) and all(isinstance(word, str) for word in words)):
			return -1

		if len(coefs) != len(words):
			return -1
		total = 0
		for coef, word in zip(coefs, words):
			total += len(word) * coef
		return total

	@staticmethod
	def enumerate_evaluate(coefs, words):
		"""
		Compute the sum of the lengths of every words in a given list weighted by a list of coefficients using enumerate.
	
	        Args:
	        coefs (list): List of coefficients.
	        words (list): List of words.
	
	        Returns:
	        int: Sum of the lengths of words weighted by coefficients, or -1 if the lists have different lengths.
	        """

		if not (isinstance(coefs, list)):
			return -1
		for coef in coefs:
			if not type(coef) in [int, float, complex]:
				return -1
		if not (isinstance(words, list) and all(isinstance(word, str) for word in words)):
			return -1

		if len(coefs) != len(words):
			return -1
		total = 0
		for i, word in enumerate(words):
			total += len(word) * coefs[i]
		return total

if __name__ == "__main__":
	words = ["Le", "Lorem", "Ipsum", "est", "simple"]
	coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
	print(Evaluator.zip_evaluate(coefs, words))

	words = ["Le", "Lorem", "Ipsum", "n’", "est", "pas", "simple"]
	coefs = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]
	print(Evaluator.enumerate_evaluate(coefs, words))
