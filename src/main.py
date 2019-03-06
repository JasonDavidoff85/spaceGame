from gunship import Gunship
import random

class GameBoard:
	def __init__(self, mapSize):
		self.gameBoard = []
		for i in range(0,mapSize[0]):
			self.gameBoard.append([0]*mapSize[1])

	def isSpaceAvailible(self,x,y):
		# returns bool
		return self.gameBoard[x][y] == 0

	def getPlacementLocation(self):
		# returns (x and y location as list)
		# calls isSpaceAvailble()
		while True:
			x = random.randrange(len(self.gameBoard))
			y = random.randrange(len(self.gameBoard[0]))
			if self.isSpaceAvailible(x,y):
				return([x,y])

	def placeElements(self,numA,numF,numR,numS):
		while numA > 0:
			coord = self.getPlacementLocation()
			self.gameBoard[coord[0]][coord[1]] = 1
			numA -= 1
		while numF > 0:
			coord = self.getPlacementLocation()
			self.gameBoard[coord[0]][coord[1]] = 2
			numF -= 1
		while numR > 0:
			coord = self.getPlacementLocation()
			self.gameBoard[coord[0]][coord[1]] = 3
			numR -= 1
		while numS > 0:
			coord = self.getPlacementLocation()
			self.gameBoard[coord[0]][coord[1]] = 4
			numS -= 1

	#==== Utility Functions =============
	def printBoard(self):
		for i in self.gameBoard:
			print(i)

def setupGame():
	mapSize = (9,9) #same as 9x9
	#implement ratio based on map size for following
	numAstroids  = 3
	numFuel = 2
	numRockets = 1
	numShips = 2

	#==set up game here==
	Map = GameBoard(mapSize) #create map
	#create game elements
	Map.placeElements(numAstroids,numFuel,numRockets,numShips)
	Map.printBoard()
	#create enemies
	#place enemines
	samus = Gunship() #create Samus
	#place samus
	main()

def main():
	return 1

if __name__ == '__main__':
    setupGame()
