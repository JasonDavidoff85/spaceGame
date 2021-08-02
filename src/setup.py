from gameboard import GameBoard
from gunship import Gunship
from spacePirates import *

mapSize = (10,10)
Map = GameBoard(mapSize) #create map

def setupGame():

	totalUnits = (mapSize[0]*mapSize[1])
	#==set up game here==
	

	Samus = Gunship() #create Samus
	Samus.setLocation(Map.getPlacementLocation())
	Map.gameBoard[Samus.location[0]][Samus.location[1]] = 8 #Place Samus

	#create game elements [astroids, fuel, rockets, ships]
	Map.placeElements(Map.amountOfElements(mapSize))

	#create enemies
	amountOfPirates = round((0.08)*totalUnits)
	amountOfCaptains = round((0.02)*totalUnits)
	spacePirate = [Grunt() for i in range(0,amountOfPirates)]
	pirateCaptain = [Captain() for i in range(0,amountOfCaptains)]

	#place enemines
	Map.placeEnemies(spacePirate,spacePirate[0].enemyType)
	Map.placeEnemies(pirateCaptain,pirateCaptain[0].enemyType)

	# ==============test calls===================
	Map.printBoard() # testing call
	Map.printNumOfElements(totalUnits) # testing call
	print(Map.enemiesRemaining()) # will be used in program l8r
	print(Map.checkMap()) # testing call
	print("Total of check:", sum(Map.checkMap())) # testing call
