import random

def guessing_game():
	secret_number = random.randint(1, 99)
	trials = 0

	while True:
		guess = input("What's your guess between 1 and 99?\n>> ")

		if guess.lower() == "exit":
			print("Goodbye!")
			break

		trials += 1

		try:
			guess = int(guess)
		except ValueError:
			print("That's not a number.")
			continue

		if guess == secret_number:
			if secret_number == 42:
				print("The answer to the ultimate question of life, the universe and everything is 42.")
			if trials == 1:
				print("Congratulations! You got it on your first try!")
			else:
				print("Congratulations, you've got it!")
				print("You won in", trials ,"attempts!")
			break
		elif guess < secret_number:
			print("Too low!")
		else:
			print("Too high!")

if __name__ == "__main__":
	print("This is an interactive guessing game!")
	print("You have to enter a number between 1 and 99 to find out the secret number.")
	print("Type 'exit' to end the game.")
	print("Good luck!\n")
	guessing_game()
