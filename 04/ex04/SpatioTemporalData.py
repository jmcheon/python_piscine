import pandas as pd
from FileLoader import FileLoader

class SpatioTemporalData:
	"""
	when(location), where(date)
	"""
	
	def __init__(self, df ):
		self.df = df

	def when(self, location):
		"""
		it takes a location as an argument and returns a list containing the
		years where games were held in the given location,
		"""
		years = self.df.loc[self.df['City'] == location, 'Year'].unique()
		return years

	def where(self, date):
		"""
		it takes a date as an argument and returns the location where the
		Olympics took place in the given year.
		"""
		location = self.df.loc[self.df['Year'] == date, 'City'].unique()
		return location


if __name__ == "__main__":
	loader = FileLoader()
	data = loader.load("../athlete_events.csv")
	sp = SpatioTemporalData(data)
	print(sp.where(1896)) 	# Output [’Athina’]
	print(sp.where(2016)) 	# Output [’Rio de Janeiro’]
	print(sp.when('Athina')) # Output [2004, 1906, 1896]
	print(sp.when('Paris')) # Output [1900, 1924]

	print(sp.where(2000)) # output is: ['Sydney']
	print(sp.where(1980)) # output is: ['Lake Placid', 'Moskva'] If a single of these locations is returned it's ok.
	print(sp.when('London')) # output is: [2012, 1948, 1908]
