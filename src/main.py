from gunship import Gunship

class GameBoard:
	def __init__(self, mapSize):
		self.gameBoard = []
		for i in range(0,int(mapSize[0])):
			self.gameBoard.append([0]*int(mapSize[-1]))

	def isSpaceAvailible(xy):
		return 0

	def placeAstroids(self):
		return 0

	#==== Utility Functions =============
	def printBoard(self):
		for i in self.gameBoard:
			print(i)

def setupGame():
	mapSize = "9x9"
	#==set up game here==
	Map = GameBoard(mapSize) #create map
	Map.printBoard()
	#create astroids
	#create refulling stations
	#create rocket locations	
	#create abondoned ships (essentially chests)
	#create enemies
	#place enemines
	samus = Gunship() #create Samus
	samus.printStats()
	#place samus
	main()

def main():
	return 1

if __name__ == '__main__':
    setupGame()
