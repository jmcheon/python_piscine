import sys
from datetime import datetime
from recipe import Recipe

class Book:
	"""
	• name (str): name of the book,
	• last_update (datetime): the date of the last update,
	• creation_date (datetime): the creation date,
	• recipes_list (dict): a dictionnary with 3 keys: "starter", "lunch", "dessert".
	"""

	def __init__(self, name):
		self.name = name
		self.last_update = datetime.now() 
		self.creation_date = self.last_update 
		self.recipes_list= {"starter" : [], "lunch" : [], "dessert" : []}

	def get_recipe_by_name(self, name):
		"""Prints a recipe with the name \texttt{name} and returns the instance"""
		if isinstance(name, str) and len(name) > 0:
			for lst in self.recipes_list.values():
				for elem in lst:
					if elem.name == name:
						print(elem)
						return elem
			print(name, "doesn't exist in the recipes_list.")
		else:
			print("name value is invalid.")

	def get_recipes_by_types(self, recipe_type):
		"""Get all recipe names for a given recipe_type """
		name_list = []
		# recipe_type validation check
		if (isinstance(recipe_type, str) and len(recipe_type) != 0 and recipe_type in ("starter", "lunch", "dessert")):
			for key, lst in self.recipes_list.items():
				if key == recipe_type:
					for elem in lst:
						name_list.append(elem.name)
		else:
			print("recipe_type value is invalid.")
		return name_list

	def add_recipe(self, recipe):
		"""Add a recipe to the boo"""
		if isinstance(recipe, Recipe):
			if recipe.recipe_type in self.recipes_list:
				self.recipes_list[recipe.recipe_type].append(recipe)
				print(type(self.recipes_list[recipe.recipe_type][0]))
				self.last_update = datetime.now()
			else:
				print("Recipe type is not valid.")
		else:
			print("Invalid type of Recipe as argument.")
