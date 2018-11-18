from mapMatrixClass import mapMatrixClass
import random


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
					self.removeWall(i,j,"N")
					if(j != self.ySize-1):
						self.removeWall(i,j+1,"S")
				if(random.randint(0,1) == 1):
					 self.removeWall(i,j,"E")
					 if(i != self.xSize-1):
						 self.removeWall(i+1,j,"W")
				if(random.randint(0,1) == 1):
					 self.removeWall(i,j,"S")
					 if(j != 0):
						 self.removeWall(i,j-1,"N")
				if(random.randint(0,1) == 1):
					self.removeWall(i,j,"W")
					if(i !=0):
						self.removeWall(i-1,j,"E")

	def generateMapEdge(self):
		for i in range(0,self.xSize):
			self.setSolidWall(i,self.ySize-1,"N")
			self.setSolidWall(i,0,"S")
		for i in range(0,self.ySize):
			self.setSolidWall(0,i,"W")
			self.setSolidWall(self.xSize-1,i,"E")

	def prepareTable(self):		#tablica testowa 10x10
		self.setSolidWall(0,0,"W")
		self.setSolidWall(0,0,"S")
		self.setSolidWall(0,1,"W")
		self.setSolidWall(0,2,"W")
		self.setSolidWall(0,3,"W")
		self.setSolidWall(0,4,"W")
		self.setSolidWall(0,5,"W")
		self.setSolidWall(0,6,"W")
		self.setSolidWall(0,6,"N")
		self.setSolidWall(0,7,"W")
		self.setSolidWall(0,7,"S")
		self.setSolidWall(0,8,"W")
		self.setSolidWall(0,9,"W")
		self.setSolidWall(0,9,"N")

		self.setSolidWall(1,0,"S")
		self.setSolidWall(1,6,"N")
		self.setSolidWall(1,7,"S")
		self.setSolidWall(1,7,"E")
		self.setSolidWall(1,8,"E")
		self.setSolidWall(1,9,"N")

		self.setSolidWall(2,0,"S")
		self.setSolidWall(2,5,"E")
		self.setSolidWall(2,6,"E")
		self.setSolidWall(2,7,"W")
		self.setSolidWall(2,8,"W")
		self.setSolidWall(2,8,"N")
		self.setSolidWall(2,9,"S")
		self.setSolidWall(2,9,"N")

		self.setSolidWall(3,0,"S")
		self.setSolidWall(3,2,"E")
		self.setSolidWall(3,4,"N")
		self.setSolidWall(3,5,"S")
		self.setSolidWall(3,5,"W")
		self.setSolidWall(3,6,"W")
		self.setSolidWall(3,6,"N")
		self.setSolidWall(3,6,"E")
		self.setSolidWall(3,7,"S")
		self.setSolidWall(3,8,"N")
		self.setSolidWall(3,8,"E")
		self.setSolidWall(3,9,"N")
		self.setSolidWall(3,9,"S")

		self.setSolidWall(4,0,"S")
		self.setSolidWall(4,1,"E")
		self.setSolidWall(4,2,"N")
		self.setSolidWall(4,2,"W")
		self.setSolidWall(4,3,"S")
		self.setSolidWall(4,4,"N")
		self.setSolidWall(4,5,"S")
		self.setSolidWall(4,6,"W")
		self.setSolidWall(4,6,"E")
		self.setSolidWall(4,7,"N")
		self.setSolidWall(4,8,"E")
		self.setSolidWall(4,8,"S")
		self.setSolidWall(4,8,"W")
		self.setSolidWall(4,9,"E")
		self.setSolidWall(4,9,"N")

		self.setSolidWall(5,0,"S")
		self.setSolidWall(5,0,"N")
		self.setSolidWall(5,1,"S")
		self.setSolidWall(5,1,"E")
		self.setSolidWall(5,1,"W")
		self.setSolidWall(5,2,"N")
		self.setSolidWall(5,2,"E")
		self.setSolidWall(5,3,"S")
		self.setSolidWall(5,4,"N")
		self.setSolidWall(5,5,"S")
		self.setSolidWall(5,5,"E")
		self.setSolidWall(5,5,"N")
		self.setSolidWall(5,6,"N")
		self.setSolidWall(5,6,"E")
		self.setSolidWall(5,6,"S")
		self.setSolidWall(5,6,"W")
		self.setSolidWall(5,7,"S")
		self.setSolidWall(5,8,"W")
		self.setSolidWall(5,9,"N")
		self.setSolidWall(5,9,"W")

		self.setSolidWall(6,0,"S")
		self.setSolidWall(6,1,"E")
		self.setSolidWall(6,1,"W")
		self.setSolidWall(6,2,"E")
		self.setSolidWall(6,2,"W")
		self.setSolidWall(6,5,"W")
		self.setSolidWall(6,6,"W")
		self.setSolidWall(6,9,"N")

		self.setSolidWall(7,0,"S")
		self.setSolidWall(7,0,"E")
		self.setSolidWall(7,1,"E")
		self.setSolidWall(7,1,"W")
		self.setSolidWall(7,2,"W")
		self.setSolidWall(7,2,"N")
		self.setSolidWall(7,3,"N")
		self.setSolidWall(7,3,"S")
		self.setSolidWall(7,3,"E")
		self.setSolidWall(7,4,"S")
		self.setSolidWall(7,7,"E")
		self.setSolidWall(7,9,"N")

		self.setSolidWall(8,0,"S")
		self.setSolidWall(8,0,"W")
		self.setSolidWall(8,1,"W")
		self.setSolidWall(8,1,"N")
		self.setSolidWall(8,2,"S")
		self.setSolidWall(8,2,"E")
		self.setSolidWall(8,3,"E")
		self.setSolidWall(8,3,"W")
		self.setSolidWall(8,4,"E")
		self.setSolidWall(8,6,"E")
		self.setSolidWall(8,6,"N")
		self.setSolidWall(8,7,"N")
		self.setSolidWall(8,7,"S")
		self.setSolidWall(8,7,"W")
		self.setSolidWall(8,8,"S")
		self.setSolidWall(8,9,"N")

		self.setSolidWall(9,0,"S")
		self.setSolidWall(9,0,"E")
		self.setSolidWall(9,1,"E")
		self.setSolidWall(9,2,"E")
		self.setSolidWall(9,2,"W")
		self.setSolidWall(9,3,"W")
		self.setSolidWall(9,3,"E")
		self.setSolidWall(9,4,"E")
		self.setSolidWall(9,4,"W")
		self.setSolidWall(9,5,"E")
		self.setSolidWall(9,5,"N")
		self.setSolidWall(9,6,"S")
		self.setSolidWall(9,6,"E")
		self.setSolidWall(9,6,"W")
		self.setSolidWall(9,7,"N")
		self.setSolidWall(9,7,"E")
		self.setSolidWall(9,8,"S")
		self.setSolidWall(9,8,"E")
		self.setSolidWall(9,9,"E")
		self.setSolidWall(9,9,"N")
