class Gunship:
	def __init__(self):
		self.shields = 100
		self.health = 50
		self.energy = 1000
		self.rockets = 0
		self.location = None

	def printStats(self):
		print("health:", self.health)
		print("shields:", self.shields)
		print("energy:", self.energy)
		print("rockets:", self.rockets)

	def setLocation(self,coord):
		self.location = [coord[0],coord[1]]

	def move(self, map):
		validDirs = ["nw","n","ne","w","e","sw","s","se"]
		print("What direction do you want to move in?")
		print("\tNW N NE\n\tW     E\n\tSW S SE")
		dir = input(">> ")
		dir = dir.lower()
		if dir in validDirs:
			print("How far in that direction?")
			dis = int(input(">> "))
			map.gameBoard[self.location[0]][self.location[1]] = 0
			if dir == "n":
				if map.inBounds(self.location[0] - dis, self.location[1]):
					self.location[0] -= dis
				else:
					print("Out of bounds")
			elif dir == "w":
				if map.inBounds(self.location[0], self.location[1] - dis):
					self.location[1] -= dis
				else:
					print("Out of bounds")
			elif dir == "s":
				if map.inBounds(self.location[0] + dis, self.location[1]):
					self.location[0] += dis
				else:
					print("Out of bounds")
			elif dir == "e":
				if map.inBounds(self.location[0], self.location[1] + dis):
					self.location[1] += dis
				else:
					print("Out of bounds")
			elif dir == "nw":
				if map.inBounds(self.location[0] + dis, self.location[1] + dis):
					self.location[0] += dis
					self.location[1] += dis
				else:
					print("Out of bounds")
			elif dir == "ne":
				if map.inBounds(self.location[0] + dis, self.location[1] + dis):
					self.location[0] += dis
					self.location[1] += dis
				else:
					print("Out of bounds")
			elif dir == "sw":
				if map.inBounds(self.location[0] + dis, self.location[1] + dis):
					self.location[0] += dis
					self.location[1] += dis
				else:
					print("Out of bounds")
			elif dir == "se":
				if map.inBounds(self.location[0] + dis, self.location[1] + dis):
					self.location[0] += dis
					self.location[1] += dis
				else:
					print("Out of bounds")
			else:
				print("Not valid direction")

			if map.isOccupied(self.location):
					map.gameOver("Hyper space collision!\nIf only you knew where you were heading!")

			map.gameBoard[self.location[0]][self.location[1]] = 8

