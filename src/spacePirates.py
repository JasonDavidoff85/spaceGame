from itertools import count

class SpacePirates:
	piratesRemaining = 0
	captainsRemaining = 0
	
	def __init__(self):
		self.piratesRemaining += 1
		self.captainsRemaining += 1


class Grunt(SpacePirates):
	pirate_ids = count(0)
	def __init__(self):
		self.id = next(self.pirate_ids)
		self.enemyType = "Grunt"
		self.shields = 75
		self.health = 40
		self.rockets = 5

class Captain(SpacePirates):
	captain_ids = count(0)
	def __init__(self):
		self.id = next(self.captain_ids)
		self.enemyType = "Captain"
		self.shields = 120
		self.health = 60
		self.rockets = 8