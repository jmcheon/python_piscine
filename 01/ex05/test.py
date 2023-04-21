from the_bank import Account, Bank

if __name__ == "__main__":

	# add test
	bank = Bank()
	bank.add(Account(
		'Jane',
		zip='911-745',
		value=1000.0,
		ref='1044618427ff2782f0bbece0abd05f31'
	))
	
	jhon = Account(
	    'Jhon',
	    zip='911-745',
	    value=1000.0,
	    ref='1044618427ff2782f0bbece0abd05f31'
	)
	
	bank.add(jhon)

	print("testing a valid transfer")
	print(jhon.value)
	bank.transfer("Jane", "Jhon", 500)
	print(jhon.value)


	bank.transfer("Jane", "Jhon", 1000)
	print(jhon.value)


#	john = Account(
#		'William John',
#		zip='100-064',
#		brother="heyhey",
#		value=6460.0,
#		ref='58ba2b9954cd278eda8a84147ca73c87',
#		info=None,
#		other='This is the vice president of the corporation',
#		lol = "hihi"
#	)
#	bank.add(john)
#	bank.fix_account(john)
#	bank.fix_account('William John')
#	print(john.__dict__.items())
#
#
#	john2 = Account(
#		'William John',
#		zip='100-064',
#		rother="heyhey",
#		value=6460.0,
#		ref='58ba2b9954cd278eda8a84147ca73c87',
#		info=None,
#		other='This is the vice president of the corporation',
#	)
#	bank.add(john2)
#	print("fix:", bank.fix_account(john2))
#
#	john3 = Account(
#		'William John',
#		zip='100-064',
#		rother="heyhey",
#		ref='58ba2b9954cd278eda8a84147ca73c87',
#		info=None,
#		other='This is the vice president of the corporation',
#		lol = "lolilol"
#	)
#	bank.add(john3)
#	print("fix:", bank.fix_account(john3))
