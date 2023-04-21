class Account(object):
	ID_COUNT = 1
	def __init__(self, name, **kwargs):
		self.__dict__.update(kwargs)

		self.id = self.ID_COUNT
		Account.ID_COUNT += 1
		self.name = name
		if not hasattr(self, 'value'):
			self.value = 0

		if self.value < 0:
			raise AttributeError("Attribute value cannot be negative.")
		if not isinstance(self.name, str):
			raise AttributeError("Attribute name must be a str object.")

	def transfer(self, amount):
		self.value += amount


class Bank(object):
	"""The bank"""
	def __init__(self):
		self.accounts = []

	def check_corrupted(self, account):
		#print(account.__dict__.items())
		# an even number of attributes,
		if len(account.__dict__) % 2 == 0:
			print("there should be an even number of attributes")
			return True

		# no attribute name, id and value,
		if not all(hasattr(account, attr) for attr in ['name', 'id', 'value']):
			print("account should have attributes of 'name', 'id', 'value'")
			return True

		# an attribute starting with b,
		if len([attr for attr in account.__dict__.keys() if attr.startswith('b')]) > 0:
			print(account.name, "account has an attribute starting with 'b'")
			return True

		# no attribute starting with zip or addr,
		if len([attr for attr in account.__dict__.keys() if attr.startswith('zip') or attr.startswith('addr')]) < 1:
			print(account.name, "account should have attributes starting with 'zip' and 'addr'")
			return True

		# name not being a string,
		if not isinstance(account.name, str):
			print("Wrong format of account name")
			return True

		# id not being an int,
		if not isinstance(account.id, int):
			print("account id should be integers")
			return True

		# value not being an int or a float.
		if not isinstance(account.value, (int, float)):
			return True
		

	def add(self, new_account):
		""" Add new_account in the Bank
		@new_account: Account() new account to append
		@return True if success, False if an error occured
		"""
		# test if new_account is an Account() instance and if
		# it can be appended to the attribute accounts
		# ... Your code ...
		# print("new account:", new_account.__dict__.items())
		if isinstance(new_account, Account) and new_account not in self.accounts:
			self.accounts.append(new_account)
			return True
		return False

	# A transaction is invalid if amount < 0 or if the amount is larger than the balance of
	# the account. Prior to the transfer, the validity of the 2 accounts (origin and dest) are
	# checked (according to the list of criteria above). A transfer between the same account
	# (bank.transfer(’Wiliam John’, ’William John’)) is valid but there is no fund movement.
	def transfer(self, origin, dest, amount):
		"""" Perform the fund transfer
		@origin: str(name) of the first account
		@dest: str(name) of the destination account
		@amount: float(amount) amount to transfer
		@return True if success, False if an error occured
		"""
		origin_account = None
		dest_account = None

		for acc in self.accounts:
			if acc.name == origin:
				origin_account = acc
			if acc.name == dest:
				dest_account = acc

		if origin_account == None or dest_account == None:
			print("Account not found")
			return False

		if self.check_corrupted(origin_account) or self.check_corrupted(dest_account):
			print("Corrupted account")
			return False

		if amount < 0 or origin_account.value < amount:
			print("Invalid amount input")
			return False
		origin_account.transfer(-amount)
		dest_account.transfer(amount)
		print("Transfer succeded")
		return True


	# fix_account recovers a corrupted account if it parameter name correspond to the
	# attribute name of one of the account in accounts (attribute of Bank). If name is not a
	# string or does not corresponded to an account name, the method return False.
	def fix_account(self, name):
		""" fix account associated to name if corrupted
		@name: str(name) of the account
		@return True if success, False if an error occured
		"""

		if not isinstance(name, str):
			return False
		account = None
		for acc in self.accounts:
			if acc.name == name:
				account = acc
		if account == None:
			return False

		filtered_account = {key : value for key, value in account.__dict__.items() if value is not None}
		account.__dict__.clear()
		account.__dict__.update(filtered_account)
		keys = list(account.__dict__.keys())
		#print(keys)

		for key in keys:
			if key.startswith('b'):
				#print(account.__dict__[key], "deleted")
				del account.__dict__[key]

		if len([attr for attr in account.__dict__.keys() if attr.startswith('zip') or attr.startswith('addr')]) > 0:
			return False

		if not all(hasattr(account, attr) for attr in ['name', 'id', 'value']):
			return False 

		try:
			account.__dict__['name'] = str(account.__dict__['name'])
		except:
			return False
		try:
			account.__dict__['id'] = id(account.__dict__['id'])
		except:
			return False

		if len(account.__dict__) % 2 == 0:
			return False 
		return True
