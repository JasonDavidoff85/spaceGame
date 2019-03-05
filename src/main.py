from gunship import Gunship
import random

class GameBoard:
	def __init__(self, mapSize):
		self.gameBoard = []
		for i in range(0,mapSize[0]):
			self.gameBoard.append([0]*mapSize[1])

	def isSpaceAvailible(xy):
		while 
		return True #returns bool

	def getPlacementLocation():
		

	def placeAstroids(self, num):
		x = random.randrange(len(self.gameBoard))
		y = random.randrange(len(self.gameBoard[0]))
		print(x)
		print(y)

	#==== Utility Functions =============
	def printBoard(self):
		for i in self.gameBoard:
			print(i)

def setupGame():
	mapSize = (10,9) #same as 9x9
	#implement ratio based on map size for following
	numAstroids  = 10



	#==set up game here==
	Map = GameBoard(mapSize) #create map
	Map.printBoard()
	Map.placeAstroids(numAstroids)#create astroids
	#create refulling stations
	#create rocket locations	
	#create abondoned ships (essentially chests)
	#create enemies
	#place enemines
	samus = Gunship() #create Samus
	#place samus
	main()

def main():
	return 1

if __name__ == '__main__':
    setupGame()
