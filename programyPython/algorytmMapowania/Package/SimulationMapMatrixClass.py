import random

from MapMatrixClass import MapMatrixClass
from DirectionEnum import DirectionEnum as Direction
from PositionClass import PositionClass

class SimulationMapMatrixClass(MapMatrixClass):
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
						position = PositionClass()
						position.x = i
						position.y = j
						self.removeWall(position,Direction.MAP_BOTTOM)
				if(random.randint(0,1) == 1):
					 self.removeWall(i,j,Direction.MAP_RIGHT)
					 if(i != self.xSize-1):
						 position = PositionClass()
						 position.x = i
 						 position.y = j
						 self.removeWall(position,Direction.MAP_LEFT)
				if(random.randint(0,1) == 1):
					 self.removeWall(position,Direction.MAP_BOTTOM)
					 if(j != 0):
						 position = PositionClass()
						 position.x = i
 						 position.y = j
						 self.removeWall(position,Direction.MAP_TOP)
				if(random.randint(0,1) == 1):
					self.removeWall(position,Direction.MAP_LEFT)
					if(i !=0):
						position = PositionClass()
						position.x = i
						position.y = j
						self.removeWall(position,Direction.MAP_RIGHT)

	def generateMapEdge(self):
		position = PositionClass()
		for position.x in range(0,self.xSize):
			position.y = self.ySize - 1
			self.setWall(position,Direction.MAP_TOP)
			position.y = 0
			self.setWall(position,Direction.MAP_BOTTOM)
		for position.y in range(0,self.ySize):
			position.x = 0
			self.setWall(position,Direction.MAP_LEFT)
			position.x = self.xSize - 1
			self.setWall(position,Direction.MAP_RIGHT)
