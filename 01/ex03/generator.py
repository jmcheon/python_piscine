import random

def generator(text, sep=" ", option=None):
	"""
	Splits the text according to sep value and yield the substrings.
	option precise if a action is performed to the substrings before it is yielded.
	"""	
	if not (isinstance(text, str) and option in [None, "shuffle", "ordered", "unique"]):
		yield "ERROR"
		return
	separated_list = text.split(sep)

	if option == None:
		for elem in separated_list:
			yield elem
	elif option == "shuffle":
		for i in range(len(separated_list) - 1, 0, -1):
			j = random.randint(0, i)
			separated_list[i], separated_list[j] = separated_list[j], separated_list[i]
		for elem in separated_list:
			yield elem
	elif option == "ordered":
		for elem in sorted(separated_list):
			yield elem
	elif option == "unique":
		#print(separated_list)
		for elem in set(separated_list):
			yield elem


if __name__ == "__main__":
	text = "Le Lorem Ipsum est simplement du faux texte."
	for word in generator(text, sep=" ", option="shuffle"):
	#for word in generator(text, sep=" ", option="ordered"):
	#text = "Lorem Ipsum Lorem Ipsum"
	#for word in generator(text, sep=" ", option="unique"):
		print(word)
