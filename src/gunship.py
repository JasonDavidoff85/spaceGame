class Gunship:
	def __init__(self):
		self.shields = 100
		self.health = 50
		self.energy = 300
		self.rockets = 0

	def printStats(self):
		print("health:", self.health)
		print("shields:", self.shields)
		print("energy:", self.energy)
		print("rockets:", self.rockets)

	def setLocation(self,coord):
		self.location = [coord[0],coord[1]]

