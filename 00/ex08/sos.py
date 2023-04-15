import sys

morse_code_dict = {
    'A': '.-',   'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.',   'H': '....', 'I': '..',   'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--',    'N': '-.',   'O': '---',   'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...',   'T': '-',    'U': '..-',   'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--',  'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': '/'
}


def get_morse_code(input_str):
	morse_code_list = []
	for char in input_str:
		if not char.isalnum() and not char.isspace():
			print("ERROR")
			return None
		char_upper = char.upper()
		if char_upper in morse_code_dict:
			morse_code_list.append(morse_code_dict[char_upper])
	output = ' '.join(morse_code_list)
	print(output)




if __name__ == "__main__":
	if len(sys.argv) == 2:
		get_morse_code(sys.argv[1])
	elif len(sys.argv) > 2:
		merged_str = ' '.join(sys.argv[1:])
		get_morse_code(merged_str)

