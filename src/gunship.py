class Gunship:
	def __init__(self):
		self.location = [5,5]
		self.shields = 100
		self.health = 50
		self.energy = 300
		self.rockets = 0

	def printStats(self):
		print("health:", self.health)
		print("shields:", self.shields)
		print("energy:", self.energy)
		print("rockets:", self.rockets)

