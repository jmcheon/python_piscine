from time import time
from time import sleep

def ft_progress(lst):
	"""Function to generate a text-based progress bar for a loop."""
	total_items = len(lst)
	start_time = time()
	
	for i, elem in enumerate(lst):
		sleep(0.005)
		
		progress = (i + 1) / total_items * 100
		elapsed_time = time() - start_time
		eta = (elapsed_time / (i + 1)) * (total_items - (i + 1))
	
		# Update progress bar
		if int(progress) != 100:
	        	progress_bar = "[{:<50}]".format("=" * int(progress / 2) + ">")
		else:
	        	progress_bar = "[{:<50}]".format("=" * int(progress / 2))
		print("ETA: {:.2f}s [ {:>3}%][{}] {}/{} | elapsed time {:.2f}s".format(
			eta, int(progress), progress_bar, i + 1, total_items, elapsed_time), end="\r")
		yield elem

def ex1():
	listy = range(1, 2)
	#print("listy:", list(listy))
	ret = 0
	for elem in ft_progress(listy):
		ret += (elem + 3) % 5
		sleep(0.01)
	print()
	print(ret)

def ex2():
	listy = range(1200)
	#print("listy:", list(listy))
	ret = 0
	for elem in ft_progress(listy):
		ret += elem
		sleep(0.005)
	print()
	print(ret)

if __name__ == "__main__":
	ex2()
