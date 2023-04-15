import sys
#recipe = { "ingredients": [], "meal": "", "prep_time": }

Sandwich = { "ingredients" : ["ham", "bread", "cheese", "tomatoes"], "meal" : "lunch", "prep_time" : 10}
Cake = { "ingredients" : ["flour", "sugar", "eggs"], "meal" : "dessert", "prep_time" : 60}
Salad = { "ingredients" : ["avocado", "arugula", "tomatoes", "spinach"], "meal" : "lunch", "prep_time" : 15}
cookbook = {"Sandwich" : Sandwich, "Cake" : Cake, "Salad" : Salad}

def print_recipe_names():
	for recipe_name in cookbook.keys():
		print(recipe_name)

def print_recipe_details(recipe_name):
	if recipe_name in cookbook:
		print("Recipe for", recipe_name, ":")
		print("   Ingredients list:", cookbook[recipe_name]["ingredients"])
		print("   To be eaten for", cookbook[recipe_name]["meal"])
		print("   Takes", cookbook[recipe_name]["prep_time"],"minutes of cooking.")
	else:
		print("Recipe for", recipe_name, "doesn't exist in cookbook!")


def delete_recipe(recipe_name):
	if recipe_name in cookbook:
		del cookbook[recipe_name] 
		print(recipe_name, "has been deleted from the cookbook.")
	else:
		print("Recipe for", recipe_name, "doesn't exist in cookbook!")

def is_valid_number(value):
	if not value.strip():
		print("The value can't be empty.")
		return False
	try:
		int(value)
		return True
	except ValueError:
		pass
	try:
		float(value)
		return True
	except ValueError:
		pass
	if '.' in value:
		return False
	return False 

def add_recipe():
	new_recipe = {"ingredients" : [], "meal" : None, "prep_time" : None}

	print("Enter a name:")
	while True:
		recipe_name = input()
		if recipe_name.strip() == "":
			print("The value can't be empty.")
		else:
			recipe_name = recipe_name.strip()
			break

	print("Enter ingredients:")
	while True:
		ingredient = input()
		if ingredient == "":
			if len(new_recipe["ingredients"]) != 0:
				break
		elif ingredient.strip() == "":
			print("The value can't be empty.")
		elif ingredient in new_recipe["ingredients"]:
			print(ingredient, "already exists in the recipe. Please enter a differenc ingredient.")
		else:
			new_recipe["ingredients"].append(ingredient.strip())

	print("Enter a meal type:")
	while True:
		meal = input()
		if meal.strip() == "":
			print("The value can't be empty.")
		else:
			new_recipe["meal"] = meal.strip()
			break

	print("Enter a preparation time:")
	while True:
		prep_time = input()
		if is_valid_number(prep_time) == True:
			new_recipe["prep_time"] = prep_time 
			break
		else:
			print("The value should be a number.")
	cookbook[recipe_name] = new_recipe

def print_option_list():
	print("List of available option:")
	print("   1: Add a recipe")
	print("   2: Delete a recipe")
	print("   3: Print a recipe")
	print("   4: Print the cookbook")
	print("   5: Quit")

def select_one_option(option):
	if option == 1:
		add_recipe()
	elif option == 2:
		print("Please enter a recipe name to delete:")
		while True:
			recipe_name = input()
			if recipe_name.strip() == "":
				print("The value can't be empty.")
			else:
				recipe_name = recipe_name.strip()
				break
		delete_recipe(recipe_name)
	elif option == 3:
		print("Please enter a recipe name to get its details:")
		while True:
			recipe_name = input()
			if recipe_name.strip() == "":
				print("The value can't be empty.")
			else:
				recipe_name = recipe_name.strip()
				break
		print_recipe_details(recipe_name)
	elif option == 4:
		print_recipe_names()
	elif option == 5:
		print("Cookbook closed. Goodbye !")
		sys.exit(0)

def check_prompt_input():
	option_list = range(1, 6)
	num = input()
	if num.isdigit():
		option = int(num)
		if option in option_list:
			select_one_option(option)
		else:
			print("Sorry, this option does not exist.")
			print_option_list()
	else:
		print("Sorry, this option does not exist.")
		print_option_list()


if __name__ == "__main__":
	print("Welcome to the Python Cookbook !")
	print_option_list()
	while True:
		print("\nPlease select an option:")
		check_prompt_input()
