import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class MyPlotLib:
	"""
	• histogram(data, features): plots one histogram for each numerical feature in
	the list,
	• density(data, features): plots the density curve of each numerical feature in
	the list,
	• pair_plot(data, features): plots a matrix of subplots (also called scatter plot
	matrix). On each subplot shows a scatter plot of one numerical variable against
	another one. The main diagonal of this matrix shows simple histograms.
	• box_plot(data, features): displays a box plot for each numerical variable in the
	dataset.
	"""

	def __init__(self) -> None:
		pass

	def histogram(self, data, features):
		"""
		it plots one histogram for each numerical feature in the list
		"""
		numerical_features = data.select_dtypes(include=['float64', 'int64']).columns.intersection(features)
		if len(numerical_features) == 0:
			print("No numerical features selected for histogram")
			return
		fig, ax = plt.subplots()
		data[numerical_features].hist(ax=ax, bins=30)
		plt.show()

	def density(self, data, features):
		"""
		it plots the density curve of each numerical feature in the list
		"""
		# Get the numerical features
		numerical_cols = data.select_dtypes(include=['float64', 'int64']).columns.tolist()
		
		# Filter the features to include only those that are numerical
		features = [f for f in features if f in numerical_cols]
		if len(features) == 0:
			print("No numerical features selected for density curve")
			return
		
		# Plot the density curves for each feature
		for feature in features:
			sns.kdeplot(data=data[feature], label=feature)
		plt.legend()
		plt.show()

	def pair_plot(self, data, features):
		"""
		it plots a matrix of subplots (also called scatter plot matrix).
		On each subplot shows a scatter plot of one numerical variable against another one.
		The main diagonal of this matrix shows simple histograms.
		"""
		numerical_cols = data.select_dtypes(include=['int', 'float']).columns
		numerical_features = [f for f in features if f in numerical_cols]
		if len(numerical_features) == 0:
			print("No numerical features selected for pair plot")
			return
		# Create a scatter plot matrix of all pairwise combinations of numerical features
		pd.plotting.scatter_matrix(data[numerical_features], diagonal='hist')
		plt.show()
	
	def box_plot(self, data, features):
		"""
		it displays a box plot for each numerical variable in the dataset.
		"""
		# plot box plot for each numerical feature
		numerical_cols = data.select_dtypes(include=['int', 'float']).columns
		numerical_features = [f for f in features if f in numerical_cols]
		if len(numerical_features) == 0:
			print("No numerical features selected for box plot")
			return
		if len(numerical_features) == 1:
			data[numerical_features[0]].plot.box()
		else:
			data[numerical_features].plot.box()
		plt.show()

if __name__ == "__main__":
	data = pd.read_csv('../athlete_events.csv')
	lst = ['Height', 'Weight']
	lst2 = ['Weight', 'Height']

	myplot = MyPlotLib()
	
	myplot.histogram(data, lst)
	myplot.density(data, lst)
	myplot.pair_plot(data, lst2)
	myplot.box_plot(data, lst2)
