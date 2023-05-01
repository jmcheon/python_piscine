import sys
import argparse
import numpy as np
from csvreader import CsvReader

class KmeansClustering:

	def __init__(self, max_iter=20, ncentroid=5):
		self.ncentroid = ncentroid # number of centroids
		self.max_iter = max_iter # number of max iterations to update the centroids
		self.centroids = [] # values of the centroids

	def fit(self, X):
		"""
		Run the K-means clustering algorithm.
		For the location of the initial centroids, random pick ncentroids from the dataset.
		Args:
		-----
		X: has to be an numpy.ndarray, a matrice of dimension m * n.
		Return:
		-------
		None.
		Raises:
		-------
		This function should not raise any Exception.
		"""
		# randomly select n centroids from the dataset
		selected_numbers = np.random.choice(X.shape[0], self.ncentroid, replace=False)
		self.centroids = X[selected_numbers, :]
	#	print("X.shape:", X.shape)
	#	print("array of randomly selected numbers:", selected_numbers)
	#	print(self.centroids)
	#	print("self.centroids.shape:", self.centroids.shape)
	#	print("self.centroids[:, np.newaxis, :].shape:", self.centroids[:, np.newaxis, :].shape)


		# loop through the max iterations to update the centroids
		for i in range(self.max_iter):
			# https://towardsdatascience.com/3-distances-that-every-data-scientist-should-know-59d864e5030a
			# Calculate the Euclidean distance between each point and centroid
			#distances = np.sqrt(np.sum((X - self.centroids[:, np.newaxis, :])**2, axis=2))
			#print("Euclidean distances:", distances.shape)

			# Calculate the L1 distance between each point and centroid
			distances = np.sum(np.abs(X - self.centroids[:, np.newaxis, :]), axis=2)
			#print("L1 distances shape:", distances.shape)

			clusters = np.argmin(distances, axis=0)
			#print(clusters, clusters.shape)

			# Update the centroids to the mean of each cluster
			for j in range(self.ncentroid):
				self.centroids[j] = np.mean(X[clusters==j], axis=0)
		
	def predict(self, X):
		"""
		Predict from wich cluster each datapoint belongs to.
		Args:
		-----
		X: has to be an numpy.ndarray, a matrice of dimension m * n.
		Return:
		-------
		the prediction has a numpy.ndarray, a vector of dimension m * 1.
		Raises:
		-------
		This function should not raise any Exception.
		"""
		# Calculate the L1 distance between each point and centroid
		distances = np.sum(np.abs(X - self.centroids[:, np.newaxis, :]), axis=2)
		#print("L1 distances shape:", distances.shape)

		# Assign each point to the closest centroid
		clusters = np.argmin(distances, axis=0)
		#print(clusters, clusters.shape)

def check_validation():
	parser = argparse.ArgumentParser(description='K-Means Clustering')
	parser.add_argument('args', nargs='*')
	args = parser.parse_args()
	for arg in args.args:
		key, val = arg.split('=')
		if key not in ['filepath', 'max_iter', 'ncentroid']:
			print(f"Invalid input: invalid key: {key}")
			return False
		if key == 'max_iter' or key == 'ncentroid':
			try:
				kwargs[key] = int(val)
			except ValueError:
				print(f"Invalid input: {key} should be a integer value")
				return False
		else:
			kwargs[key] = val
	#print(kwargs)
	return True

if __name__ == "__main__":
	if len(sys.argv) != 4:
		#python Kmeans.py filepath='<path_to_solar_system_census_csv_file>' ncentroid=4 max_iter=30
		print("Usage: python Kmean.py [filepath] [max_iter] [ncentroid]")
		print("Example:")
		print("\tpython Kmeans.py filepath='<path_to_solar_system_census_csv_file>' ncentroid=4 max_iter=30")
	else:
		kwargs = {}
		if not check_validation():
			exit()
		filepath = kwargs['filepath']
		ncentroid = kwargs['ncentroid']
		max_iter = kwargs['max_iter']
		k = KmeansClustering(max_iter=max_iter, ncentroid=ncentroid)
		with CsvReader(filepath, header=True) as reader:
			if reader == None:
				print("File is corrupted or missing")
			else:
				X = np.array(reader.getdata())
				k.fit(X.astype(float))
				print(k.centroids)
