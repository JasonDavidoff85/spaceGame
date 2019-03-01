class spacePirates:
	def __init__(self, enemyNum):
		# if enemy num is odd, it is a bady
		if ((enemyNum % 2) == 0):
			self.enemyNum = enemyNum
			self.shields = 75
			self.health = 40
			self.rockets = 5
		elif ((enemyNum % 1) != 0):
			self.enemyNum = enemyNum
			self.shields = 120
			self.health = 60
			self.rockets = 8
		else:
			raise Exception('enemy num not valid')
