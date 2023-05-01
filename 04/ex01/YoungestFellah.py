import pandas as pd
from FileLoader import FileLoader

def youngest_fellah(df, year):
	# Filter the data by year
	df = df.loc[df['Year'] == year]

	# Filter by sex pour female and male
	female_df = df[df['Sex'] == 'F']
	male_df = df[df['Sex'] == 'M']

	# find the youngest female and male
	female_max_age = female_df['Age'].min()
	male_max_age = male_df['Age'].min()

	result = {'f': female_max_age, 'm': male_max_age}
	return result


if __name__ == "__main__":
	loader = FileLoader()
	data = loader.load("../athlete_events.csv")

	print(youngest_fellah(data, 2004)) #{’f’: 13.0, ’m’: 14.0}
	print(youngest_fellah(data, 1992)) # output is: "{'f': 12.0, 'm': 11.0}"
	print(youngest_fellah(data, 2004)) # output is: "{'f': 13.0, 'm': 14.0}"
	print(youngest_fellah(data, 2010)) # output is: "{'f': 15.0, 'm': 15.0}"
	print(youngest_fellah(data, 2003)) # output is: "{'f': nan, 'm': nan}"
