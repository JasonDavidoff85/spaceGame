from gunship import Gunship
from spacePirates import SpacePirates
import random

class GameBoard:
	def __init__(self, mapSize):
		self.gameBoard = []
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
		self.numAstroids = round((0.09)*(mapSize[0] * mapSize[1]))
		self.numFuel = round((0.06)*(mapSize[0] * mapSize[1]))
		self.numRockets = round((0.08)*(mapSize[0] * mapSize[1]))
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
			elif _type == "Captain":
				self.gameBoard[coord[0]][coord[1]] = 6

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

def setupGame():
	mapSize = (10,10)
	totalUnits = (mapSize[0]*mapSize[1])
	#==set up game here==
	Map = GameBoard(mapSize) #create map

	Samus = Gunship() #create Samus
	Samus.setLocation(Map.getPlacementLocation())
	Map.gameBoard[Samus.location[0]][Samus.location[1]] = 8 #Place Samus

	#create game elements [astroids, fuel, rockets, ships]
	Map.placeElements(Map.amountOfElements(mapSize))

	#create enemies
	amountOfPirates = round((0.08)*totalUnits)
	amountOfCaptains = round((0.02)*totalUnits)
	spacePirate = [SpacePirates("Grunt") for i in range(0,amountOfPirates)]
	pirateCaptain = [SpacePirates("Captain") for i in range(0,amountOfCaptains)]

	#place enemines
	Map.placeEnemies(spacePirate,spacePirate[0].enemyType)
	Map.placeEnemies(pirateCaptain,pirateCaptain[0].enemyType)

	# ==============test calls===================
	Map.printBoard() # testing call
	Map.printNumOfElements(totalUnits) # testing call
	print(SpacePirates.enemiesRemaining()) # will be used in program l8r
	print(Map.checkMap()) # testing call
	print("Total of check:", sum(Map.checkMap())) # testing call

	main()

def main():
	return 1

if __name__ == '__main__':
    setupGame()
