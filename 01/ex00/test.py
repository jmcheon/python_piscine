from book import Book
from recipe import Recipe


if __name__ == "__main__":

	b = Book("Korean recipe book")
	print(b.creation_date)

	egg_roll = Recipe("egg roll", 1, 5, ["egg", "salt", "green onion", "sesame oil"], "roll roll", "dessert")
	tteokbokki = Recipe("tteokbokki", 2, 15, ["tteo", "gochujang", "sugar", "corn syrup", "chili powder"], "yammy", "lunch")
	jajangmyeon = Recipe("jajangmyeon", 4, 30, ["noodle", "salt", "chunjang", "onion", "vegetable oil", "carrot"], "very tasty", "lunch")
	#to_print = str(tourte)
	#print(to_print)

	b.add_recipe(tteokbokki)
	b.add_recipe(egg_roll)
	b.add_recipe(jajangmyeon)
	print(b.last_update)

	b.get_recipe_by_name("egg roll")
	b.get_recipe_by_name("tteokbokki")
	b.get_recipe_by_name("jajangmyeon")
	print(b.get_recipes_by_types("lunch"))
	print(b.get_recipes_by_types("starter"))
	print(b.get_recipes_by_types("dinner"))
	print(b.last_update)

