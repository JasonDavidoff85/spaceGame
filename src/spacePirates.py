from itertools import count

class SpacePirates:
	pirate_ids = count(0)
	captain_ids = count(0)

	piratesRemaining = 0
	captainsRemaining = 0

	def __init__(self, enemyNum):
		global piratesRemaining
		global captainsRemaining

		if (enemyNum == "Grunt"):
			self.id = next(self.pirate_ids)
			self.enemyType = enemyNum
			self.shields = 75
			self.health = 40
			self.rockets = 5
			piratesRemaining = self.id

		elif (enemyNum == "Captain"):
			self.id = next(self.captain_ids)
			self.enemyType = enemyNum
			self.shields = 120
			self.health = 60
			self.rockets = 8
			captainsRemaining = self.id

	def enemiesRemaining():
		return ([piratesRemaining + 1,captainsRemaining + 1])