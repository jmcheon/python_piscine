import pandas as pd
from FileLoader import FileLoader

def how_many_medals(df, name):
	df = df.loc[df['Name'] == name].copy()
	df.fillna('NA', inplace=True)
	#print(df)

	medal_count = df.groupby(['Year', 'Medal'])['Medal'].count()
	#print(medal_count, end="\n\n")

	result = {}
	for (year, medal), count in medal_count.items():
		if year not in result:
			result[year] = {'G': 0, 'S': 0, 'B': 0}
		if medal == 'Gold':
			result[year]['G'] = count
		elif medal == 'Silver':
			result[year]['S'] = count
		elif medal == 'Bronze':
			result[year]['B'] = count
	return result
	
	


if __name__ == "__main__":
	loader = FileLoader()
	data = loader.load("../athlete_events.csv")
	print(how_many_medals(data, 'Kjetil Andr Aamodt'))
	print(how_many_medals(data, 'Gary Abraham')) #  the output is: "{1976: {'G': 0, 'S': 0, 'B': 0}, 1980: {'G': 0, 'S': 0, 'B': 1}}"
	print(how_many_medals(data, 'Yekaterina Konstantinovna Abramova')) #  the output is "{2006: {'G': 0, 'S': 0, 'B': 1}, 2010: {'G': 0, 'S': 0, 'B': 0}}"
	print(how_many_medals(data, 'Kristin Otto')) #  the output is: "{1988: {'G': 6, 'S': 0, 'B': 0}}"
