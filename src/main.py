from gunship import Gunship
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

	#==== Utility Functions =============
	def printBoard(self):
		for i in self.gameBoard:
			print(i)

	def printNumOfElements(self,total):
		print("Astroids:",self.numAstroids," %" + str(round((self.numAstroids/total) * 100)))
		print("Astroids:",self.numFuel," %" + str(round((self.numFuel/total) * 100)))
		print("Astroids:",self.numRockets," %" + str(round((self.numRockets/total) * 100)))
		print("Astroids:",self.numShips," %" + str(round((self.numShips/total) * 100)))

def setupGame():
	mapSize = (10,10)
	#==set up game here==
	Map = GameBoard(mapSize) #create map

	samus = Gunship() #create Samus
	samus.setLocation(Map.getPlacementLocation())
	Map.gameBoard[samus.location[0]][samus.location[1]] = 8

	#create game elements [astroids, fuel, rockets, ships]
	Map.placeElements(Map.amountOfElements(mapSize))

	#create enemies
	#place enemines

	Map.printBoard() # testing call
	Map.printNumOfElements(mapSize[0]*mapSize[1]) # testing call

	main()

def main():
	return 1

if __name__ == '__main__':
    setupGame()