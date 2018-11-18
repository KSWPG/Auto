import random

from mapMatrixClass import mapMatrixClass
from DirectionEnum import DirectionEnum as Direction

class simulationMapMatrixClass(mapMatrixClass):
	def generateRandomMap(self):
		self.setAllWallExist()
		self.randomlyRemoveTheWalls()
		self.generateMapEdge()

	def setAllWallExist(self):
		for i in range(0,self.xSize):
			for j in range(0,self.ySize):
				self.mapMatrix[i][j] = 15

	def randomlyRemoveTheWalls(self):
		for i in range(0,self.xSize):
			for j in range(0,self.ySize):
				if(random.randint(0,1) == 1):
					self.removeWall(i,j,Direction.MAP_TOP)
					if(j != self.ySize-1):
						self.removeWall(i,j+1,Direction.MAP_BOTTOM)
				if(random.randint(0,1) == 1):
					 self.removeWall(i,j,Direction.MAP_RIGHT)
					 if(i != self.xSize-1):
						 self.removeWall(i+1,j,Direction.MAP_LEFT)
				if(random.randint(0,1) == 1):
					 self.removeWall(i,j,Direction.MAP_BOTTOM)
					 if(j != 0):
						 self.removeWall(i,j-1,Direction.MAP_TOP)
				if(random.randint(0,1) == 1):
					self.removeWall(i,j,Direction.MAP_LEFT)
					if(i !=0):
						self.removeWall(i-1,j,Direction.MAP_RIGHT)

	def generateMapEdge(self):
		for i in range(0,self.xSize):
			self.setWall(i,self.ySize-1,Direction.MAP_TOP)
			self.setWall(i,0,Direction.MAP_BOTTOM)
		for i in range(0,self.ySize):
			self.setWall(0,i,Direction.MAP_LEFT)
			self.setWall(self.xSize-1,i,Direction.MAP_RIGHT)

	def prepareTable(self):		#tablica testowa 10x10
		self.setWall(0,0,Direction.MAP_LEFT)
		self.setWall(0,0,Direction.MAP_BOTTOM)
		self.setWall(0,1,Direction.MAP_LEFT)
		self.setWall(0,2,Direction.MAP_LEFT)
		self.setWall(0,3,Direction.MAP_LEFT)
		self.setWall(0,4,Direction.MAP_LEFT)
		self.setWall(0,5,Direction.MAP_LEFT)
		self.setWall(0,6,Direction.MAP_LEFT)
		self.setWall(0,6,Direction.MAP_TOP)
		self.setWall(0,7,Direction.MAP_LEFT)
		self.setWall(0,7,Direction.MAP_BOTTOM)
		self.setWall(0,8,Direction.MAP_LEFT)
		self.setWall(0,9,Direction.MAP_LEFT)
		self.setWall(0,9,Direction.MAP_TOP)

		self.setWall(1,0,Direction.MAP_BOTTOM)
		self.setWall(1,6,Direction.MAP_TOP)
		self.setWall(1,7,Direction.MAP_BOTTOM)
		self.setWall(1,7,Direction.MAP_RIGHT)
		self.setWall(1,8,Direction.MAP_RIGHT)
		self.setWall(1,9,Direction.MAP_TOP)

		self.setWall(2,0,Direction.MAP_BOTTOM)
		self.setWall(2,5,Direction.MAP_RIGHT)
		self.setWall(2,6,Direction.MAP_RIGHT)
		self.setWall(2,7,Direction.MAP_LEFT)
		self.setWall(2,8,Direction.MAP_LEFT)
		self.setWall(2,8,Direction.MAP_TOP)
		self.setWall(2,9,Direction.MAP_BOTTOM)
		self.setWall(2,9,Direction.MAP_TOP)

		self.setWall(3,0,Direction.MAP_BOTTOM)
		self.setWall(3,2,Direction.MAP_RIGHT)
		self.setWall(3,4,Direction.MAP_TOP)
		self.setWall(3,5,Direction.MAP_BOTTOM)
		self.setWall(3,5,Direction.MAP_LEFT)
		self.setWall(3,6,Direction.MAP_LEFT)
		self.setWall(3,6,Direction.MAP_TOP)
		self.setWall(3,6,Direction.MAP_RIGHT)
		self.setWall(3,7,Direction.MAP_BOTTOM)
		self.setWall(3,8,Direction.MAP_TOP)
		self.setWall(3,8,Direction.MAP_RIGHT)
		self.setWall(3,9,Direction.MAP_TOP)
		self.setWall(3,9,Direction.MAP_BOTTOM)

		self.setWall(4,0,Direction.MAP_BOTTOM)
		self.setWall(4,1,Direction.MAP_RIGHT)
		self.setWall(4,2,Direction.MAP_TOP)
		self.setWall(4,2,Direction.MAP_LEFT)
		self.setWall(4,3,Direction.MAP_BOTTOM)
		self.setWall(4,4,Direction.MAP_TOP)
		self.setWall(4,5,Direction.MAP_BOTTOM)
		self.setWall(4,6,Direction.MAP_LEFT)
		self.setWall(4,6,Direction.MAP_RIGHT)
		self.setWall(4,7,Direction.MAP_TOP)
		self.setWall(4,8,Direction.MAP_RIGHT)
		self.setWall(4,8,Direction.MAP_BOTTOM)
		self.setWall(4,8,Direction.MAP_LEFT)
		self.setWall(4,9,Direction.MAP_RIGHT)
		self.setWall(4,9,Direction.MAP_TOP)

		self.setWall(5,0,Direction.MAP_BOTTOM)
		self.setWall(5,0,Direction.MAP_TOP)
		self.setWall(5,1,Direction.MAP_BOTTOM)
		self.setWall(5,1,Direction.MAP_RIGHT)
		self.setWall(5,1,Direction.MAP_LEFT)
		self.setWall(5,2,Direction.MAP_TOP)
		self.setWall(5,2,Direction.MAP_RIGHT)
		self.setWall(5,3,Direction.MAP_BOTTOM)
		self.setWall(5,4,Direction.MAP_TOP)
		self.setWall(5,5,Direction.MAP_BOTTOM)
		self.setWall(5,5,Direction.MAP_RIGHT)
		self.setWall(5,5,Direction.MAP_TOP)
		self.setWall(5,6,Direction.MAP_TOP)
		self.setWall(5,6,Direction.MAP_RIGHT)
		self.setWall(5,6,Direction.MAP_BOTTOM)
		self.setWall(5,6,Direction.MAP_LEFT)
		self.setWall(5,7,Direction.MAP_BOTTOM)
		self.setWall(5,8,Direction.MAP_LEFT)
		self.setWall(5,9,Direction.MAP_TOP)
		self.setWall(5,9,Direction.MAP_LEFT)

		self.setWall(6,0,Direction.MAP_BOTTOM)
		self.setWall(6,1,Direction.MAP_RIGHT)
		self.setWall(6,1,Direction.MAP_LEFT)
		self.setWall(6,2,Direction.MAP_RIGHT)
		self.setWall(6,2,Direction.MAP_LEFT)
		self.setWall(6,5,Direction.MAP_LEFT)
		self.setWall(6,6,Direction.MAP_LEFT)
		self.setWall(6,9,Direction.MAP_TOP)

		self.setWall(7,0,Direction.MAP_BOTTOM)
		self.setWall(7,0,Direction.MAP_RIGHT)
		self.setWall(7,1,Direction.MAP_RIGHT)
		self.setWall(7,1,Direction.MAP_LEFT)
		self.setWall(7,2,Direction.MAP_LEFT)
		self.setWall(7,2,Direction.MAP_TOP)
		self.setWall(7,3,Direction.MAP_TOP)
		self.setWall(7,3,Direction.MAP_BOTTOM)
		self.setWall(7,3,Direction.MAP_RIGHT)
		self.setWall(7,4,Direction.MAP_BOTTOM)
		self.setWall(7,7,Direction.MAP_RIGHT)
		self.setWall(7,9,Direction.MAP_TOP)

		self.setWall(8,0,Direction.MAP_BOTTOM)
		self.setWall(8,0,Direction.MAP_LEFT)
		self.setWall(8,1,Direction.MAP_LEFT)
		self.setWall(8,1,Direction.MAP_TOP)
		self.setWall(8,2,Direction.MAP_BOTTOM)
		self.setWall(8,2,Direction.MAP_RIGHT)
		self.setWall(8,3,Direction.MAP_RIGHT)
		self.setWall(8,3,Direction.MAP_LEFT)
		self.setWall(8,4,Direction.MAP_RIGHT)
		self.setWall(8,6,Direction.MAP_RIGHT)
		self.setWall(8,6,Direction.MAP_TOP)
		self.setWall(8,7,Direction.MAP_TOP)
		self.setWall(8,7,Direction.MAP_BOTTOM)
		self.setWall(8,7,Direction.MAP_LEFT)
		self.setWall(8,8,Direction.MAP_BOTTOM)
		self.setWall(8,9,Direction.MAP_TOP)

		self.setWall(9,0,Direction.MAP_BOTTOM)
		self.setWall(9,0,Direction.MAP_RIGHT)
		self.setWall(9,1,Direction.MAP_RIGHT)
		self.setWall(9,2,Direction.MAP_RIGHT)
		self.setWall(9,2,Direction.MAP_LEFT)
		self.setWall(9,3,Direction.MAP_LEFT)
		self.setWall(9,3,Direction.MAP_RIGHT)
		self.setWall(9,4,Direction.MAP_RIGHT)
		self.setWall(9,4,Direction.MAP_LEFT)
		self.setWall(9,5,Direction.MAP_RIGHT)
		self.setWall(9,5,Direction.MAP_TOP)
		self.setWall(9,6,Direction.MAP_BOTTOM)
		self.setWall(9,6,Direction.MAP_RIGHT)
		self.setWall(9,6,Direction.MAP_LEFT)
		self.setWall(9,7,Direction.MAP_TOP)
		self.setWall(9,7,Direction.MAP_RIGHT)
		self.setWall(9,8,Direction.MAP_BOTTOM)
		self.setWall(9,8,Direction.MAP_RIGHT)
		self.setWall(9,9,Direction.MAP_RIGHT)
		self.setWall(9,9,Direction.MAP_TOP)
