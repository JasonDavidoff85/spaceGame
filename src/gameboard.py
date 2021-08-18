import random
VIEWSIZE = 5
class GameBoard:
	def __init__(self, mapSize):
		self.gameBoard = []
		self.numEnemies = 0
		self.mapSize = mapSize
		for i in range(0,mapSize[0]):
			self.gameBoard.append([0]*mapSize[1])

	def isSpaceAvailible(self,x,y):
		# returns bool
		return not(self.gameBoard[x][y] != 0)

	def getPlacementLocation(self):
		# returns (x and y location as list)
		# calls isSpaceAvailble()
		while True:
			x = random.randrange(len(self.gameBoard))
			y = random.randrange(len(self.gameBoard[0]))
			if self.isSpaceAvailible(x,y):
				return([x,y])

	def amountOfElements(self,mapSize):
		# returns list of each amount of elements
		self.numAstroids = round((0.06)*(mapSize[0] * mapSize[1]))
		self.numFuel = round((0.03)*(mapSize[0] * mapSize[1]))
		self.numRockets = round((0.05)*(mapSize[0] * mapSize[1]))
		self.numShips = round((0.03)*(mapSize[0] * mapSize[1]))
		return [self.numAstroids,self.numFuel,self.numRockets,self.numShips]

	def placeOnBoard(self,coord,symbol):
		self.gameBoard[coord[0]][coord[1]] = symbol

	def placeElements(self,num):
		while num[0] > 0:
			coord = self.getPlacementLocation()
			self.gameBoard[coord[0]][coord[1]] = 1
			num[0] -= 1
		while num[1] > 0:
			coord = self.getPlacementLocation()
			self.gameBoard[coord[0]][coord[1]] = 2
			num[1] -= 1
		while num[2] > 0:
			coord = self.getPlacementLocation()
			self.gameBoard[coord[0]][coord[1]] = 3
			num[2] -= 1
		while num[3] > 0:
			coord = self.getPlacementLocation()
			self.gameBoard[coord[0]][coord[1]] = 4
			num[3] -= 1

	def placeEnemies(self,enemies,_type):
		for enemy in enemies:
			coord = self.getPlacementLocation()
			if _type == "Grunt":
				self.gameBoard[coord[0]][coord[1]] = 5
				self.numEnemies += 1
			elif _type == "Captain":
				self.gameBoard[coord[0]][coord[1]] = 6
				self.numEnemies += 1

	def enemiesRemaining(self):
		return self.numEnemies

	def inBounds(self, *location):
		return location[0] >= 0 and location[0] < self.mapSize[0] and location[1] >= 0 and location[1] < self.mapSize[1]

	def isOccupied(self, location):
		return self.gameBoard[location[0]][location[1]] != 0

	def gameOver(self, msg):
		print("=====Game over=====")
		print(msg)
		exit(0)


	def show(self, location):
		x = (location[0] // VIEWSIZE) * VIEWSIZE
		y = (location[1] // VIEWSIZE) * VIEWSIZE
		for i in range(x, x + VIEWSIZE):
			if i <= self.mapSize[0]:
				print(self.gameBoard[i][y:y+VIEWSIZE])


	#==== Utility Functions =============
	def printBoard(self):
		for i in self.gameBoard:
			print(i)

	def printNumOfElements(self,total):
		print("Astroids:",self.numAstroids," %" + str(round((self.numAstroids/total) * 100)))
		print("Fuel:    ",self.numFuel," %" + str(round((self.numFuel/total) * 100)))
		print("Rockets: ",self.numRockets," %" + str(round((self.numRockets/total) * 100)))
		print("Ships:   ",self.numShips," %" + str(round((self.numShips/total) * 100)))

	def checkMap(self):
		totalValues = [0,0,0,0,0,0,0,0]
		for row in self.gameBoard:
			for i in range(0,7):
				totalValues[i] += row.count(i)
			totalValues[7] += row.count(8)
		return totalValues