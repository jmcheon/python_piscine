import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class Komparator:
	"""
	compare_box_plots(self, categorical_var, numerical_var)
	density(self, categorical_var, numerical_var)
	compare_histograms(self, categorical_var, numerical_var)
	"""

	def __init__(self, data):
		self.data = data

	@staticmethod
	def check_validation(plot_type, categorical_var, numerical_var):
		if not isinstance(categorical_var, str) or not isinstance(numerical_var, str):
			print("Invalid input: string variables required")
			return False
		categorical_cols = data.select_dtypes(include=['object']).columns
		categorical_features = [f for f in [categorical_var] if f in categorical_cols]
		if len(categorical_features) == 0:
			print(f"No categorical features selected for {plot_type} plot")
			return False
		numerical_cols = data.select_dtypes(include=['int', 'float']).columns
		numerical_features = [f for f in [numerical_var] if f in numerical_cols]
		if len(numerical_features) == 0:
			print(f"No numerical features selected for {plot_type} plot")
			return False
		return True

	def compare_box_plots(self, categorical_var, numerical_var):
		"""
		it displays a series of box plots to compare how the distribution of the numerical variable changes
		if we only consider the subpopulation which belongs to each category. There should
		be as many box plots as categories. For example, with Sex and Height, we would
		compare the height distributions of men vs. women with two box plots.
		"""
		if not self.check_validation("box", categorical_var, numerical_var):
			return
		categories = self.data[categorical_var].dropna().unique()
		boxplot_data = {}
		for category in categories:
			subset = self.data[self.data[categorical_var] == category][numerical_var]
			boxplot_data[category] = subset
		boxplot_df = pd.DataFrame(boxplot_data)
		boxplot_df.plot.box(figsize=(10, 6))
		plt.title(f"Box plot of {numerical_var} for each category of {categorical_var}")
		plt.show()

	def density(self, categorical_var, numerical_var):
		"""
		it displays the density of the 	numerical variable.
		Each subpopulation should be represented by a separate curve on the graph.
		"""
		if not self.check_validation("density", categorical_var, numerical_var):
			return
		categories = self.data[categorical_var].dropna().unique()
		for category in categories:
			subset = self.data[self.data[categorical_var] == category][numerical_var]
			subset.plot(kind='density', figsize=(10, 6), label=category, legend=True)
		plt.xlabel(numerical_var)
		plt.title(f"Density curve of {numerical_var} for each category of {categorical_var}")
		plt.show()

	def compare_histograms(self, categorical_var, numerical_var):
		"""
		it plots the numerical variable in a separate histogram for each category.
		As an extra, you can use overlapping histograms with a color code
		"""
		if not self.check_validation("histogram", categorical_var, numerical_var):
			return
		categories = self.data[categorical_var].dropna().unique()
		colors = ['blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan']
		fig, ax = plt.subplots(figsize=(10, 6))
		for i, category in enumerate(categories):
			subset = self.data[self.data[categorical_var] == category][numerical_var]
			ax.hist(subset, bins=20, alpha=0.5, color=colors[i], label=category)
		ax.legend(loc='upper right')
		plt.xlabel(numerical_var)
		plt.title(f"Histogram plot of {numerical_var} for each category of {categorical_var}")
		plt.show()

def compare_plots(categorical_var, numerical_var):
	komparator.compare_box_plots(categorical_var, numerical_var)
	komparator.density(categorical_var, numerical_var)
	komparator.compare_histograms(categorical_var, numerical_var)

def ex1():
	komparator.compare_box_plots('Medal', 'Age')
	komparator.density('Medal', 'Weight')
	komparator.compare_histograms('Medal', 'Height')

if __name__ == "__main__":
	data = pd.read_csv('../athlete_events.csv')
	komparator = Komparator(data)
	compare_plots('Sex', 'Height')
	#ex1()
