import numpy as np
import sys

class mapMatrixClass():
	def __init__(self,x,y):
		self.xSize = x
		self.ySize = y
		self.mapMatrix = np.zeros((self.xSize,self.ySize),dtype=np.byte)

	def setSolidWall(self,x,y,direction):
		self.checkVariablesForMatrix(x,y)
		if direction == "N":
			self.mapMatrix[x][y] = self.mapMatrix[x][y] | 8
		elif direction == "E":
			 self.mapMatrix[x][y] = self.mapMatrix[x][y] | 4
		elif direction == "S":
			self.mapMatrix[x][y] = self.mapMatrix[x][y] | 2
		elif direction == "W":
			self.mapMatrix[x][y] = self.mapMatrix[x][y] | 1
		else:
			raise Exception("Wrong parameter for direction")

	def isWallExist(self,x,y,direction):
		self.checkVariablesForMatrix(x,y)
		if direction == "N" :
			if self.mapMatrix[x][y] & 8 == 8: return True
		elif direction == "E" :
			if self.mapMatrix[x][y] & 4 == 4: return True
		elif direction == "S" :
			if self.mapMatrix[x][y] & 2 == 2: return True
		elif direction == "W" :
			if self.mapMatrix[x][y] & 1 == 1: return True
		else:
			raise Exception("Wrong parameter for direction")
		return False

	def setVisited(self,x,y):
		self.checkVariablesForMatrix(x,y)
		self.mapMatrix[x][y] = self.mapMatrix[x][y] | 16

	def wasVisited(self,x,y):
		self.checkVariablesForMatrix(x,y)
		if self.mapMatrix[x][y] & 16 == 16: return True
		else: return False

	def setNotAvailable(self,x,y):
		self.checkVariablesForMatrix(x,y)
		self.mapMatrix[x][y] = self.mapMatrix[x][y] | 32

	def isNotAvailable(self,x,y):
		self.checkVariablesForMatrix(x,y)
		if self.mapMatrix[x][y] & 32 == 32: return True
		else: return False

	def checkVariablesForMatrix(self,x,y):
		if(x < 0 or x >= self.xSize or y < 0 or y >= self.ySize):
			raise Exception("Matrix indexes outside the scope")

	def addNewRow(self,y,direction):
		if direction == "N" and y == self.ySize-1:
			self.mapMatrix = np.insert(self.mapMatrix, [self.ySize],0,axis=1)
			self.ySize = self.ySize +1
			return True
		elif direction == "S" and y == 0:
			self.mapMatrix = np.insert(self.mapMatrix, [0],0,axis=1)
			self.ySize = self.ySize +1
			return True
		else: return False

	def addNewColumn(self,x,direction):
		if direction == "E" and x == self.xSize-1:
			self.mapMatrix = np.insert(self.mapMatrix, [self.xSize],0,axis=0)
			self.xSize = self.xSize +1
			return True
		elif direction == "W" and x == 0:
			self.mapMatrix = np.insert(self.mapMatrix, [0],0,axis=0)
			self.xSize = self.xSize +1
			return True
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
