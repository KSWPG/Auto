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
			self.setWall(i,self.ySize-1,"N")
			self.setWall(i,0,"S")
		for i in range(0,self.ySize):
			self.setWall(0,i,"W")
			self.setWall(self.xSize-1,i,"E")

	def prepareTable(self):		#tablica testowa 10x10
		self.setWall(0,0,"W")
		self.setWall(0,0,"S")
		self.setWall(0,1,"W")
		self.setWall(0,2,"W")
		self.setWall(0,3,"W")
		self.setWall(0,4,"W")
		self.setWall(0,5,"W")
		self.setWall(0,6,"W")
		self.setWall(0,6,"N")
		self.setWall(0,7,"W")
		self.setWall(0,7,"S")
		self.setWall(0,8,"W")
		self.setWall(0,9,"W")
		self.setWall(0,9,"N")

		self.setWall(1,0,"S")
		self.setWall(1,6,"N")
		self.setWall(1,7,"S")
		self.setWall(1,7,"E")
		self.setWall(1,8,"E")
		self.setWall(1,9,"N")

		self.setWall(2,0,"S")
		self.setWall(2,5,"E")
		self.setWall(2,6,"E")
		self.setWall(2,7,"W")
		self.setWall(2,8,"W")
		self.setWall(2,8,"N")
		self.setWall(2,9,"S")
		self.setWall(2,9,"N")

		self.setWall(3,0,"S")
		self.setWall(3,2,"E")
		self.setWall(3,4,"N")
		self.setWall(3,5,"S")
		self.setWall(3,5,"W")
		self.setWall(3,6,"W")
		self.setWall(3,6,"N")
		self.setWall(3,6,"E")
		self.setWall(3,7,"S")
		self.setWall(3,8,"N")
		self.setWall(3,8,"E")
		self.setWall(3,9,"N")
		self.setWall(3,9,"S")

		self.setWall(4,0,"S")
		self.setWall(4,1,"E")
		self.setWall(4,2,"N")
		self.setWall(4,2,"W")
		self.setWall(4,3,"S")
		self.setWall(4,4,"N")
		self.setWall(4,5,"S")
		self.setWall(4,6,"W")
		self.setWall(4,6,"E")
		self.setWall(4,7,"N")
		self.setWall(4,8,"E")
		self.setWall(4,8,"S")
		self.setWall(4,8,"W")
		self.setWall(4,9,"E")
		self.setWall(4,9,"N")

		self.setWall(5,0,"S")
		self.setWall(5,0,"N")
		self.setWall(5,1,"S")
		self.setWall(5,1,"E")
		self.setWall(5,1,"W")
		self.setWall(5,2,"N")
		self.setWall(5,2,"E")
		self.setWall(5,3,"S")
		self.setWall(5,4,"N")
		self.setWall(5,5,"S")
		self.setWall(5,5,"E")
		self.setWall(5,5,"N")
		self.setWall(5,6,"N")
		self.setWall(5,6,"E")
		self.setWall(5,6,"S")
		self.setWall(5,6,"W")
		self.setWall(5,7,"S")
		self.setWall(5,8,"W")
		self.setWall(5,9,"N")
		self.setWall(5,9,"W")

		self.setWall(6,0,"S")
		self.setWall(6,1,"E")
		self.setWall(6,1,"W")
		self.setWall(6,2,"E")
		self.setWall(6,2,"W")
		self.setWall(6,5,"W")
		self.setWall(6,6,"W")
		self.setWall(6,9,"N")

		self.setWall(7,0,"S")
		self.setWall(7,0,"E")
		self.setWall(7,1,"E")
		self.setWall(7,1,"W")
		self.setWall(7,2,"W")
		self.setWall(7,2,"N")
		self.setWall(7,3,"N")
		self.setWall(7,3,"S")
		self.setWall(7,3,"E")
		self.setWall(7,4,"S")
		self.setWall(7,7,"E")
		self.setWall(7,9,"N")

		self.setWall(8,0,"S")
		self.setWall(8,0,"W")
		self.setWall(8,1,"W")
		self.setWall(8,1,"N")
		self.setWall(8,2,"S")
		self.setWall(8,2,"E")
		self.setWall(8,3,"E")
		self.setWall(8,3,"W")
		self.setWall(8,4,"E")
		self.setWall(8,6,"E")
		self.setWall(8,6,"N")
		self.setWall(8,7,"N")
		self.setWall(8,7,"S")
		self.setWall(8,7,"W")
		self.setWall(8,8,"S")
		self.setWall(8,9,"N")

		self.setWall(9,0,"S")
		self.setWall(9,0,"E")
		self.setWall(9,1,"E")
		self.setWall(9,2,"E")
		self.setWall(9,2,"W")
		self.setWall(9,3,"W")
		self.setWall(9,3,"E")
		self.setWall(9,4,"E")
		self.setWall(9,4,"W")
		self.setWall(9,5,"E")
		self.setWall(9,5,"N")
		self.setWall(9,6,"S")
		self.setWall(9,6,"E")
		self.setWall(9,6,"W")
		self.setWall(9,7,"N")
		self.setWall(9,7,"E")
		self.setWall(9,8,"S")
		self.setWall(9,8,"E")
		self.setWall(9,9,"E")
		self.setWall(9,9,"N")
