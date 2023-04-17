import sys

class Recipe:
	"""
	• name (str): name of the recipe
	• cooking_lvl (int): range from 1 to 5,
	• cooking_time (int): in minutes (no negative numbers),
	• ingredients (list): list of all ingredients each represented by a string,
	• description (str): description of the recipe,
	• recipe_type (str): can be "starter", "lunch" or "dessert"
	"""

	def check_valid_input(name, lvl, time, ingre, desc, recipe_type):
		# name validation check
		if not (isinstance(name, str) and len(name) != 0):
			print("name value is invalid.")
			return False

		# level validation check
		if not (isinstance(lvl, int) and (0 < lvl < 6)):
			print("cooking level value is invalid.")
			return False

		# time validation check
		if not isinstance(time, int) or time < 0:
			print("cooking time value is invalid.")
			return False

		# ingredients validation check
		if not (isinstance(ingre, list) and len(ingre) > 0):
			print("ingredients value is invalid.")
			return False
			
		# description validation check
		if not (isinstance(desc, str)):
			print("description value is invalid.")
			return False
			
		# recipe_type validation check
		if not (isinstance(recipe_type, str) and len(recipe_type) != 0 and recipe_type in ("starter", "lunch", "dessert")):
			print("recipe_type value is invalid.")
			return False
		return True

	def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
		if Recipe.check_valid_input(name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
			self.name = name
			self.cooking_lvl = cooking_lvl
			self.cooking_time = cooking_time
			self.ingredients = ingredients
			self.description = description
			self.recipe_type = recipe_type


	def __str__(self):
		"""Return the string to print with the recipe info"""
		txt = f"Recipe : {self.name}\n cooking level : {self.cooking_lvl}\n cooking time : {self.cooking_time}\n ingredients : {self.ingredients}\n description : {self.description}\n recipe type : {self.recipe_type}\n"
		"""Your code here"""
		return txt
