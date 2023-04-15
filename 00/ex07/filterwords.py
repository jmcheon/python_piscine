import sys
import string

def filterwords(S, N):
	min_length = int(N)
	words_list = S.split()
	punctuations = string.punctuation
	non_punctuation_list = []
	for word in words_list:
		word_without_punctuation = ''.join(char for char in word if char not in string.punctuation)
		non_punctuation_list.append(word_without_punctuation)
	selected_list = [word for word in non_punctuation_list if len(word) > min_length]
	print(selected_list)

if __name__ == "__main__":
	if len(sys.argv) != 3:
		print("ERROR")
	else:
		if not isinstance(sys.argv[1], str):
			print("ERROR")
			sys.exit()
		try:
			int(sys.argv[2])
		except ValueError:
			print("ERROR")
			sys.exit()
		else:
			filterwords(sys.argv[1], sys.argv[2])
	
