import matplotlib.pyplot as plt

class Player:

	def __init__(self, name):
		self.name = name
		self.properties = []

	#getter function
	def get_first_name(self):
		return self.first_name

	#Setter function
	def set_nickname(self, value):
		if not isinstance(value, str):
			raise TypeError("C'mon! !@#$ gimme a string!")
		self.nickname = value

	def add_property(self, prop):
		self.properties.append(prop)

	#def sell_property(self, prop, to):
		#Sells Property "prop" in properties list to Player
		#   "to".
	#	if prop not in to.properties:
	#		self.




class Property:

	def __init__(self, name, bids=[], owners=[]):
		self.name = name
		self.bids = bids
		self.owners = owners

	def add_owner(self, owner):
		self.owners.append(owner)
	
	def remove_owner(self, owner):
		self.owners.remove(owner)
	
	def add_bid(self, b):
		self.bids.append(b)

	def plot_bids(self):
		plt.plot(self.bids)
		plt.ylabel('Bid Prices')
		plt.show()


	

	
		
		
		



	
		
		
	

