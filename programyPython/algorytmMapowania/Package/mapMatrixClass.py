import numpy as np
import sys
import random

class mapMatrixClass():
	def __init__(self,x,y):
		self.xSize = x
		self.ySize = y
		self.mapMatrix = np.zeros((self.xSize,self.ySize),dtype=np.byte)

	def prepareTable(self):		#metoda tylko do testow tylko dla tablicy 10X10
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
		#self.setSolidWall(9,4,"N")
		self.setSolidWall(9,4,"W")
		self.setSolidWall(9,5,"E")
		#self.setSolidWall(9,5,"S")
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

	def generateRandomMap(self):
		self.generateMapEdge()
		for i in range(0,self.xSize):
			for j in range(0,self.ySize):
				if(random.randint(0,1) == 1):
					self.setSolidWall(i,j,"N")
					if(i != self.xSize-1):
						self.setSolidWall(i+1,j,"S")
				if(random.randint(0,1) == 1):
					 self.setSolidWall(i,j,"E")
					 if(j != self.ySize-1):
						 self.setSolidWall(i,j+1,"W")
				if(random.randint(0,1) == 1):
					 self.setSolidWall(i,j,"S")
					 if(i != 0):
						 self.setSolidWall(i-1,j,"N")
				if(random.randint(0,1) == 1):
					self.setSolidWall(i,j,"W")
					if(j !=0):
						self.setSolidWall(i,j-1,"E")

	def generateMapEdge(self):
		for i in range(0,self.xSize):
			self.setSolidWall(i,self.ySize-1,"N")
			self.setSolidWall(i,0,"S")
		for i in range(0,self.ySize):
			self.setSolidWall(0,i,"W")
			self.setSolidWall(self.xSize-1,i,"E")

	def setSolidWall(self,x,y,direction):
		if direction == "N" : self.mapMatrix[x][y] = self.mapMatrix[x][y] | 8
		elif direction == "E" : self.mapMatrix[x][y] = self.mapMatrix[x][y] | 4
		elif direction == "S" : self.mapMatrix[x][y] = self.mapMatrix[x][y] | 2
		elif direction == "W" : self.mapMatrix[x][y] = self.mapMatrix[x][y] | 1

	def isWallExist(self,x,y,direction):
		if direction == "N" :
			if self.mapMatrix[x][y] & 8 == 8: return True
		elif direction == "E" :
			if self.mapMatrix[x][y] & 4 == 4: return True
		elif direction == "S" :
			if self.mapMatrix[x][y] & 2 == 2: return True
		elif direction == "W" :
			if self.mapMatrix[x][y] & 1 == 1: return True
		return False

	def setVisited(self,x,y):
		self.mapMatrix[x][y] = self.mapMatrix[x][y] | 16

	def wasVisited(self,x,y):
		if self.mapMatrix[x][y] & 16 == 16: return True
		else: return False

	def setNotAvailable(self,x,y):
		self.mapMatrix[x][y] = self.mapMatrix[x][y] | 32

	def isNotAvailable(self,x,y):
		if self.mapMatrix[x][y] & 32 == 32: return True
		else: return False

	def findWayToNearestNoVisitedSpot(self,robotXposition,robotYposition):
		pathMap = np.zeros((self.xSize,self.ySize),dtype=np.byte)
		pathMap[robotXposition][robotYposition]=1

		actualValue=1
		findX=0
		findY=0
		endLoop=0

		while (endLoop==0):
			changeAmount=0
			for i in range(0,self.xSize):
				for j in range(0,self.ySize):
					if(pathMap[i][j] == actualValue):
						if(not self.isWallExist(i,j,"W")):
							if(pathMap[i-1][j]==0):
								pathMap[i-1][j]=actualValue+1
								changeAmount=changeAmount+1
								if(not self.wasVisited(i-1,j)):
									findX=i-1
									findY=j
									endLoop=1
									break
						if(not self.isWallExist(i,j,"N")):
							if(pathMap[i][j+1]==0):
								pathMap[i][j+1]=actualValue+1
								changeAmount=changeAmount+1
								if(not self.wasVisited(i,j+1)):
									findX=i
									findY=j+1
									endLoop=1
									break
						if(not self.isWallExist(i,j,"E")):
							if(pathMap[i+1][j]==0):
								pathMap[i+1][j]=actualValue+1
								changeAmount=changeAmount+1
								if(not self.wasVisited(i+1,j)):
									findX=i+1
									findY=j
									endLoop=1
									break
						if(not self.isWallExist(i,j,"S")):
							if(pathMap[i][j-1]==0):
								pathMap[i][j-1]=actualValue+1
								changeAmount=changeAmount+1
								if(not self.wasVisited(i,j-1)):
									findX=i
									findY=j-1
									endLoop=1
									break
				if(endLoop!=0):break
			actualValue = actualValue + 1
			if(changeAmount==0):
				raise Exception("Not found anymore no visited spot")

		return self.findPathTo(findX,findY,robotXposition,robotYposition)

	def findWayToNearestNoVisitedSpot2(self,robotXposition,robotYposition,course):
		pathMap = np.zeros((self.xSize,self.ySize),dtype=np.byte)
		pathMap[robotXposition][robotYposition]=1

		actualValue=1
		findX=0
		findY=0
		endLoop=0

		while (endLoop==0):
			changeAmount=0
			for i in range(0,self.xSize):
				for j in range(0,self.ySize):
					if(pathMap[i][j] == actualValue):
						if course == 0:
							if(not self.isWallExist(i,j,"W")):
								if(pathMap[i-1][j]==0):
									pathMap[i-1][j]=actualValue+1
									changeAmount=changeAmount+1
									if(not self.wasVisited(i-1,j)):
										findX=i-1
										findY=j
										endLoop=1
										break
							if(not self.isWallExist(i,j,"N")):
								if(pathMap[i][j+1]==0):
									pathMap[i][j+1]=actualValue+1
									changeAmount=changeAmount+1
									if(not self.wasVisited(i,j+1)):
										findX=i
										findY=j+1
										endLoop=1
										break
							if(not self.isWallExist(i,j,"E")):
								if(pathMap[i+1][j]==0):
									pathMap[i+1][j]=actualValue+1
									changeAmount=changeAmount+1
									if(not self.wasVisited(i+1,j)):
										findX=i+1
										findY=j
										endLoop=1
										break
							if(not self.isWallExist(i,j,"S")):
								if(pathMap[i][j-1]==0):
									pathMap[i][j-1]=actualValue+1
									changeAmount=changeAmount+1
									if(not self.wasVisited(i,j-1)):
										findX=i
										findY=j-1
										endLoop=1
										break
						elif course == 90:
							if(not self.isWallExist(i,j,"N")):
								if(pathMap[i][j+1]==0):
									pathMap[i][j+1]=actualValue+1
									changeAmount=changeAmount+1
									if(not self.wasVisited(i,j+1)):
										findX=i
										findY=j+1
										endLoop=1
										break
							if(not self.isWallExist(i,j,"E")):
								if(pathMap[i+1][j]==0):
									pathMap[i+1][j]=actualValue+1
									changeAmount=changeAmount+1
									if(not self.wasVisited(i+1,j)):
										findX=i+1
										findY=j
										endLoop=1
										break
							if(not self.isWallExist(i,j,"S")):
								if(pathMap[i][j-1]==0):
									pathMap[i][j-1]=actualValue+1
									changeAmount=changeAmount+1
									if(not self.wasVisited(i,j-1)):
										findX=i
										findY=j-1
										endLoop=1
										break
							if(not self.isWallExist(i,j,"W")):
								if(pathMap[i-1][j]==0):
									pathMap[i-1][j]=actualValue+1
									changeAmount=changeAmount+1
									if(not self.wasVisited(i-1,j)):
										findX=i-1
										findY=j
										endLoop=1
										break
						elif course == 180:
							if(not self.isWallExist(i,j,"E")):
								if(pathMap[i+1][j]==0):
									pathMap[i+1][j]=actualValue+1
									changeAmount=changeAmount+1
									if(not self.wasVisited(i+1,j)):
										findX=i+1
										findY=j
										endLoop=1
										break
							if(not self.isWallExist(i,j,"S")):
								if(pathMap[i][j-1]==0):
									pathMap[i][j-1]=actualValue+1
									changeAmount=changeAmount+1
									if(not self.wasVisited(i,j-1)):
										findX=i
										findY=j-1
										endLoop=1
										break
							if(not self.isWallExist(i,j,"W")):
								if(pathMap[i-1][j]==0):
									pathMap[i-1][j]=actualValue+1
									changeAmount=changeAmount+1
									if(not self.wasVisited(i-1,j)):
										findX=i-1
										findY=j
										endLoop=1
										break
							if(not self.isWallExist(i,j,"N")):
								if(pathMap[i][j+1]==0):
									pathMap[i][j+1]=actualValue+1
									changeAmount=changeAmount+1
									if(not self.wasVisited(i,j+1)):
										findX=i
										findY=j+1
										endLoop=1
										break
						elif course ==270:
							if(not self.isWallExist(i,j,"S")):
								if(pathMap[i][j-1]==0):
									pathMap[i][j-1]=actualValue+1
									changeAmount=changeAmount+1
									if(not self.wasVisited(i,j-1)):
										findX=i
										findY=j-1
										endLoop=1
										break
							if(not self.isWallExist(i,j,"W")):
								if(pathMap[i-1][j]==0):
									pathMap[i-1][j]=actualValue+1
									changeAmount=changeAmount+1
									if(not self.wasVisited(i-1,j)):
										findX=i-1
										findY=j
										endLoop=1
										break
							if(not self.isWallExist(i,j,"N")):
								if(pathMap[i][j+1]==0):
									pathMap[i][j+1]=actualValue+1
									changeAmount=changeAmount+1
									if(not self.wasVisited(i,j+1)):
										findX=i
										findY=j+1
										endLoop=1
										break
							if(not self.isWallExist(i,j,"E")):
								if(pathMap[i+1][j]==0):
									pathMap[i+1][j]=actualValue+1
									changeAmount=changeAmount+1
									if(not self.wasVisited(i+1,j)):
										findX=i+1
										findY=j
										endLoop=1
										break


				if(endLoop!=0):break
			actualValue = actualValue + 1
			if(changeAmount==0):
				raise Exception("Not found anymore no visited spot")

		return self.findPathTo(findX,findY,robotXposition,robotYposition)

	def findPathTo(self,pointX,pointY,fromX,fromY):
		pathMap = np.zeros((self.xSize,self.ySize),dtype=np.byte)
		pathMap[pointX][pointY] = 1
		actualValue = 1
		endLoop=0
		while (endLoop==0):
			for i in range(0,self.xSize):
				for j in range(0,self.ySize):
					if(pathMap[i][j] == actualValue):
						if(i != 0 and not self.isWallExist(i,j,"W")):
							if(pathMap[i-1][j]==0):
								pathMap[i-1][j]=actualValue+1
								if(i-1 == fromX and j == fromY):
									endLoop = 1
									break
						if(j != self.ySize-1 and not self.isWallExist(i,j,"N")):
							if(pathMap[i][j+1]==0):
								pathMap[i][j+1]=actualValue+1
								if(i == fromX and j+1 == fromY):
									endLoop = 1
									break
						if(i != self.xSize-1 and not self.isWallExist(i,j,"E")):
							if(pathMap[i+1][j]==0):
								pathMap[i+1][j]=actualValue+1
								if(i+1 == fromX and j == fromY):
									endLoop = 1
									break
						if(j !=0 and not self.isWallExist(i,j,"S")):
							if(pathMap[i][j-1]==0):
								pathMap[i][j-1]=actualValue+1
								if(i == fromX and j-1 == fromY):
									endLoop = 1
									break
				if(endLoop!=0):break
			actualValue = actualValue+1

		#print pathMap
		return pathMap

	def drawMap(self):
		sys.stdout.flush()

		for k in range(0,self.xSize):
			sys.stdout.write('____')
		print("")
		for rowNumber in range(self.ySize-1,-1,-1):
			self.drawMatrixRow(rowNumber)

	def drawMatrixRow(self,rowNumber):
		for k in range(0,2):
			for columnNumber in range(0,self.xSize):
				if(columnNumber is not 0):
					if(self.isWallExist(columnNumber,rowNumber,"W")):
						sys.stdout.write("|")
						if(k==1 and self.isWallExist(columnNumber,rowNumber,"S")): sys.stdout.write("___")
						elif(k==1 and rowNumber==0): sys.stdout.write("___")
						else: sys.stdout.write("   ")
					else:
						if(k==1 and self.isWallExist(columnNumber,rowNumber,"S")): sys.stdout.write("____")
						elif(k==1 and rowNumber==0): sys.stdout.write("____")
						else: sys.stdout.write("    ")
				else:
					sys.stdout.write("|")
					if(k==1 and self.isWallExist(columnNumber,rowNumber,"S")): sys.stdout.write("___")
					elif(k==1 and rowNumber==0): sys.stdout.write("___")
					else: sys.stdout.write("   ")
				if(columnNumber==self.xSize-1):sys.stdout.write("|")
			print("")
