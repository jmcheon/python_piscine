import my_minipack.progressbar
import my_minipack.logger



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
	machine = CoffeeMachine()
	#for i in range(0, 5):
	#	machine.make_coffee()
	machine.make_coffee()
	machine.add_water(70)

	ex2()
