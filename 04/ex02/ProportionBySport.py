import pandas as pd
from FileLoader import FileLoader

def proportion_by_sport(df, year, sport, gender):
	# Filter df by year and gender
	df = df[(df['Year'] == year) & (df['Sex'] == gender)]

	# Count the number of participants in the gender and sport
	sport_count = len(df[df['Sport'] == sport])
	gender_count = len(df)

	proportion = (sport_count / gender_count)
	return proportion


if __name__ == "__main__":
	loader = FileLoader()
	data = loader.load("../athlete_events.csv")
	print(proportion_by_sport(data, 2004, 'Tennis', 'F'), end = "\n\n") # "0.02307"
	print(proportion_by_sport(data, 2008, 'Hockey', 'F'), end = "\n\n") # "0.03284"
	print(proportion_by_sport(data, 1964, 'Biathlon', 'M'), end = "\n\n") # "0.00659"
