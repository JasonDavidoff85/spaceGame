
from setup import *

def run():
	day = 0
	while True:
		Map.show(Samus.location)
		print("samus location: (" + str(Samus.location[0]) +", " + str(Samus.location[1]) + ")")
		print("Day ", day)
		line = input(">> ")
		cmd = line.split()[0]
		if cmd == "move":
			Samus.move(Map)
		elif cmd == "help":
			if len(line.split()) < 2:
				help()
			else:
				help(line.split()[1])
		

def help(option=None):
	print("\n======help======")
	if option == None:
		print("(1) warp")
		print("(2) float")
		print("(3) fire")
		print("(4) scan")
	elif option == "warp":
		print("Uses energy to warp ship to specific location")
		print("use: warp [spaces] [direction]")
		print("ex. warp 3 NE")
	elif option == "float":
		print("No energy option to move one space in any direction")
		print("use: float [direction]")
		print("ex. float W")
	elif option == "fire":
		print("Fire a missle (missle or lazer)")
		print("Missle - launch a missle in a direction")
		print("Lazer - shoot lazer that reaches two spaces in a direction")
		print("ex. fire missle W")
		print("ex. fire lazer SE")
	else:
		print("Not a valid command")
	print("===============\n")


if __name__ == '__main__':
	setupGame()
	run()
