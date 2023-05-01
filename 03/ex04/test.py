import sys
import numpy as np
import matplotlib.pyplot as plt
from csvreader import CsvReader
from mpl_toolkits import mplot3d

def plot_1by3():
	fig, axs = plt.subplots(3, 1)
	# Create scatter images
	axs[0].scatter(index, weight)
	#axs[0].set_xlabel("height")
	axs[0].set_ylabel("weight")

	axs[1].scatter(index, height)
	#axs[1].set_xlabel("weight")
	axs[1].set_ylabel("height")

	axs[2].scatter(index, bone_density)
	#axs[2].set_xlabel("bone density")
	axs[2].set_ylabel("bone density")

	plt.show()

def plot_3by2():
	fig, axs = plt.subplots(3, 2)
	# Create scatter images
	axs[0, 0].scatter(height, weight)
	axs[0, 0].set_xlabel("height")
	axs[0, 0].set_ylabel("weight")

	axs[0, 1].scatter(height, bone_density)
	axs[0, 1].set_xlabel("height")
	axs[0, 1].set_ylabel("bone_density")

	axs[1, 0].scatter(weight, height)
	axs[1, 0].set_xlabel("weight")
	axs[1, 0].set_ylabel("height")

	axs[1, 1].scatter(weight, bone_density)
	axs[1, 1].set_xlabel("weight")
	axs[1, 1].set_ylabel("bone density")

	axs[2, 0].scatter(bone_density, height)
	axs[2, 0].set_xlabel("bone density")
	axs[2, 0].set_ylabel("height")
	
	axs[2, 1].scatter(bone_density, height)
	axs[2, 1].set_xlabel("bone density")
	axs[2, 1].set_ylabel("height")

	plt.show()

def plot_3d():
	# Create a figure and a 3D subplot
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	
	# Create a scatter plot
	ax.scatter(height, weight, bone_density)
	
	# Set labels for the axes
	ax.set_xlabel('height')
	ax.set_ylabel('weight')
	ax.set_zlabel('bone density')
	
	# Show the plot
	plt.show()

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print(f"Usage: python {sys.argv[0]} [filepath]")
		exit()

	filename = sys.argv[1]
	with CsvReader(filename, header=True) as reader:
		if reader == None:
			print("File is corrupted or missing")
			exit()
		else:
			X = reader.getdata()
			header = reader.getheader()
	
	# extract columns 'height' and 'weight' and 'bone_density' from the dataframe
	index = [row[0] for row in X]
	height = [float(row[1]) for row in X]
	weight = [float(row[2]) for row in X]
	bone_density = [float(row[3]) for row in X]

	plot_1by3()
	#plot_3by2()
	#plot_3d()
