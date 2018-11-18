import numpy as np
import sys

from DirectionEnum import DirectionEnum as Direction

class MapMatrixClass():
	def __init__(self,xSize,ySize):
		self.xSize = xSize
		self.ySize = ySize
		self.mapMatrix = np.zeros((self.xSize,self.ySize),dtype=np.byte)

	def setWallsInContiguousField(self,x,y,direction):
		self.setWall(x,y,direction)

		xForContiguousField = x
		yForContiguousField = y
		directionForContiguousField = ""

		if(direction == Direction.MAP_TOP):
			directionForContiguousField == Direction.MAP_BOTTOM
			yForContiguousField = y + 1
		elif(direction == Direction.MAP_BOTTOM):
			directionForContiguousField == Direction.MAP_TOP
			yForContiguousField = y - 1
		elif(direction == Direction.MAP_RIGHT):
			directionForContiguousField == Direction.MAP_LEFT
			xForContiguousField = x + 1
		elif(direction == Direction.MAP_LEFT):
			directionForContiguousField == Direction.MAP_RIGHT
			xForContiguousField = x - 1

		try:
			self.setWall(xForContiguousField,yForContiguousField,directionForContiguousField)
		except:
			pass

	def setWall(self,x,y,direction):
		self.checkScopeOfIndex(x,y)
		if direction == Direction.MAP_TOP:
			self.mapMatrix[x][y] = self.mapMatrix[x][y] | 8
		elif direction == Direction.MAP_RIGHT:
			 self.mapMatrix[x][y] = self.mapMatrix[x][y] | 4
		elif direction == Direction.MAP_BOTTOM:
			self.mapMatrix[x][y] = self.mapMatrix[x][y] | 2
		elif direction == Direction.MAP_LEFT:
			self.mapMatrix[x][y] = self.mapMatrix[x][y] | 1
		else:
			raise Exception("Wrong parameter for direction")

	def removeWall(self,x,y,direction):
		self.checkScopeOfIndex(x,y)
		if direction == Direction.MAP_TOP:
			self.mapMatrix[x][y] = self.mapMatrix[x][y] & 247
		elif direction == Direction.MAP_RIGHT:
			 self.mapMatrix[x][y] = self.mapMatrix[x][y] & 251
		elif direction == Direction.MAP_BOTTOM:
			self.mapMatrix[x][y] = self.mapMatrix[x][y] & 253
		elif direction == Direction.MAP_LEFT:
			self.mapMatrix[x][y] = self.mapMatrix[x][y] & 254
		else:
			raise Exception("Wrong parameter for direction")

	def isWallExist(self,x,y,direction):
		self.checkScopeOfIndex(x,y)
		if direction == Direction.MAP_TOP :
			if self.mapMatrix[x][y] & 8 == 8: return True
		elif direction == Direction.MAP_RIGHT :
			if self.mapMatrix[x][y] & 4 == 4: return True
		elif direction == Direction.MAP_BOTTOM :
			if self.mapMatrix[x][y] & 2 == 2: return True
		elif direction == Direction.MAP_LEFT :
			if self.mapMatrix[x][y] & 1 == 1: return True
		else:
			raise Exception("Wrong parameter for direction")
		return False

	def setVisited(self,x,y):
		self.checkScopeOfIndex(x,y)
		self.mapMatrix[x][y] = self.mapMatrix[x][y] | 16

	def setUnVisited(self,x,y):
		self.checkScopeOfIndex(x,y)
		self.mapMatrix[x][y] = self.mapMatrix[x][y] & 239

	def wasVisited(self,x,y):
		self.checkScopeOfIndex(x,y)
		if self.mapMatrix[x][y] & 16 == 16: return True
		else: return False

	def setNotAvailable(self,x,y):
		self.checkScopeOfIndex(x,y)
		self.mapMatrix[x][y] = self.mapMatrix[x][y] | 32

	def setAvailable(self,x,y):
		self.checkScopeOfIndex(x,y)
		self.mapMatrix[x][y] = self.mapMatrix[x][y] & 223

	def isNotAvailable(self,x,y):
		self.checkScopeOfIndex(x,y)
		if self.mapMatrix[x][y] & 32 == 32: return True
		else: return False

	def checkScopeOfIndex(self,x,y):
		if(x < 0 or x >= self.xSize or y < 0 or y >= self.ySize):
			raise Exception("Matrix indexes outside the scope")

	def addNewRowIfNeeded(self,y,direction):
		if direction == Direction.MAP_TOP and y == self.ySize-1:
			self.mapMatrix = np.insert(self.mapMatrix, [self.ySize],0,axis=1)
			self.ySize = self.ySize +1
			return True
		elif direction == Direction.MAP_BOTTOM and y == 0:
			self.mapMatrix = np.insert(self.mapMatrix, [0],0,axis=1)
			self.ySize = self.ySize +1
			return True
		else: return False

	def addNewColumnIfNeeded(self,x,direction):
		if direction == Direction.MAP_RIGHT and x == self.xSize-1:
			self.mapMatrix = np.insert(self.mapMatrix, [self.xSize],0,axis=0)
			self.xSize = self.xSize + 1
			return True
		elif direction == Direction.MAP_LEFT and x == 0:
			self.mapMatrix = np.insert(self.mapMatrix, [0],0,axis=0)
			self.xSize = self.xSize + 1
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
						if(not self.isWallExist(i,j,Direction.MAP_LEFT)):
							if(pathMap[i-1][j]==0):
								pathMap[i-1][j]=actualValue+1
								changeAmount=changeAmount+1
								if(not self.wasVisited(i-1,j)):
									findX=i-1
									findY=j
									endLoop=1
									break
						if(not self.isWallExist(i,j,Direction.MAP_TOP)):
							if(pathMap[i][j+1]==0):
								pathMap[i][j+1]=actualValue+1
								changeAmount=changeAmount+1
								if(not self.wasVisited(i,j+1)):
									findX=i
									findY=j+1
									endLoop=1
									break
						if(not self.isWallExist(i,j,Direction.MAP_RIGHT)):
							if(pathMap[i+1][j]==0):
								pathMap[i+1][j]=actualValue+1
								changeAmount=changeAmount+1
								if(not self.wasVisited(i+1,j)):
									findX=i+1
									findY=j
									endLoop=1
									break
						if(not self.isWallExist(i,j,Direction.MAP_BOTTOM)):
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
							if(not self.isWallExist(i,j,Direction.MAP_LEFT)):
								if(pathMap[i-1][j]==0):
									pathMap[i-1][j]=actualValue+1
									changeAmount=changeAmount+1
									if(not self.wasVisited(i-1,j)):
										findX=i-1
										findY=j
										endLoop=1
										break
							if(not self.isWallExist(i,j,Direction.MAP_TOP)):
								if(pathMap[i][j+1]==0):
									pathMap[i][j+1]=actualValue+1
									changeAmount=changeAmount+1
									if(not self.wasVisited(i,j+1)):
										findX=i
										findY=j+1
										endLoop=1
										break
							if(not self.isWallExist(i,j,Direction.MAP_RIGHT)):
								if(pathMap[i+1][j]==0):
									pathMap[i+1][j]=actualValue+1
									changeAmount=changeAmount+1
									if(not self.wasVisited(i+1,j)):
										findX=i+1
										findY=j
										endLoop=1
										break
							if(not self.isWallExist(i,j,Direction.MAP_BOTTOM)):
								if(pathMap[i][j-1]==0):
									pathMap[i][j-1]=actualValue+1
									changeAmount=changeAmount+1
									if(not self.wasVisited(i,j-1)):
										findX=i
										findY=j-1
										endLoop=1
										break
						elif course == 90:
							if(not self.isWallExist(i,j,Direction.MAP_TOP)):
								if(pathMap[i][j+1]==0):
									pathMap[i][j+1]=actualValue+1
									changeAmount=changeAmount+1
									if(not self.wasVisited(i,j+1)):
										findX=i
										findY=j+1
										endLoop=1
										break
							if(not self.isWallExist(i,j,Direction.MAP_RIGHT)):
								if(pathMap[i+1][j]==0):
									pathMap[i+1][j]=actualValue+1
									changeAmount=changeAmount+1
									if(not self.wasVisited(i+1,j)):
										findX=i+1
										findY=j
										endLoop=1
										break
							if(not self.isWallExist(i,j,Direction.MAP_BOTTOM)):
								if(pathMap[i][j-1]==0):
									pathMap[i][j-1]=actualValue+1
									changeAmount=changeAmount+1
									if(not self.wasVisited(i,j-1)):
										findX=i
										findY=j-1
										endLoop=1
										break
							if(not self.isWallExist(i,j,Direction.MAP_LEFT)):
								if(pathMap[i-1][j]==0):
									pathMap[i-1][j]=actualValue+1
									changeAmount=changeAmount+1
									if(not self.wasVisited(i-1,j)):
										findX=i-1
										findY=j
										endLoop=1
										break
						elif course == 180:
							if(not self.isWallExist(i,j,Direction.MAP_RIGHT)):
								if(pathMap[i+1][j]==0):
									pathMap[i+1][j]=actualValue+1
									changeAmount=changeAmount+1
									if(not self.wasVisited(i+1,j)):
										findX=i+1
										findY=j
										endLoop=1
										break
							if(not self.isWallExist(i,j,Direction.MAP_BOTTOM)):
								if(pathMap[i][j-1]==0):
									pathMap[i][j-1]=actualValue+1
									changeAmount=changeAmount+1
									if(not self.wasVisited(i,j-1)):
										findX=i
										findY=j-1
										endLoop=1
										break
							if(not self.isWallExist(i,j,Direction.MAP_LEFT)):
								if(pathMap[i-1][j]==0):
									pathMap[i-1][j]=actualValue+1
									changeAmount=changeAmount+1
									if(not self.wasVisited(i-1,j)):
										findX=i-1
										findY=j
										endLoop=1
										break
							if(not self.isWallExist(i,j,Direction.MAP_TOP)):
								if(pathMap[i][j+1]==0):
									pathMap[i][j+1]=actualValue+1
									changeAmount=changeAmount+1
									if(not self.wasVisited(i,j+1)):
										findX=i
										findY=j+1
										endLoop=1
										break
						elif course ==270:
							if(not self.isWallExist(i,j,Direction.MAP_BOTTOM)):
								if(pathMap[i][j-1]==0):
									pathMap[i][j-1]=actualValue+1
									changeAmount=changeAmount+1
									if(not self.wasVisited(i,j-1)):
										findX=i
										findY=j-1
										endLoop=1
										break
							if(not self.isWallExist(i,j,Direction.MAP_LEFT)):
								if(pathMap[i-1][j]==0):
									pathMap[i-1][j]=actualValue+1
									changeAmount=changeAmount+1
									if(not self.wasVisited(i-1,j)):
										findX=i-1
										findY=j
										endLoop=1
										break
							if(not self.isWallExist(i,j,Direction.MAP_TOP)):
								if(pathMap[i][j+1]==0):
									pathMap[i][j+1]=actualValue+1
									changeAmount=changeAmount+1
									if(not self.wasVisited(i,j+1)):
										findX=i
										findY=j+1
										endLoop=1
										break
							if(not self.isWallExist(i,j,Direction.MAP_RIGHT)):
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
						if(i != 0 and not self.isWallExist(i,j,Direction.MAP_LEFT)):
							if(pathMap[i-1][j]==0):
								pathMap[i-1][j]=actualValue+1
								if(i-1 == fromX and j == fromY):
									endLoop = 1
									break
						if(j != self.ySize-1 and not self.isWallExist(i,j,Direction.MAP_TOP)):
							if(pathMap[i][j+1]==0):
								pathMap[i][j+1]=actualValue+1
								if(i == fromX and j+1 == fromY):
									endLoop = 1
									break
						if(i != self.xSize-1 and not self.isWallExist(i,j,Direction.MAP_RIGHT)):
							if(pathMap[i+1][j]==0):
								pathMap[i+1][j]=actualValue+1
								if(i+1 == fromX and j == fromY):
									endLoop = 1
									break
						if(j !=0 and not self.isWallExist(i,j,Direction.MAP_BOTTOM)):
							if(pathMap[i][j-1]==0):
								pathMap[i][j-1]=actualValue+1
								if(i == fromX and j-1 == fromY):
									endLoop = 1
									break
				if(endLoop!=0):break
			actualValue = actualValue+1

		#print pathMap
		return pathMap

	def completeMapAfterMapping(self):
		for i in range(0,self.xSize):
			for j in range(0,self.ySize):
				if(not self.wasVisited(i,j)):
					self.setNotAvailable(i,j)

				if(i != 0 and self.isWallExist(i-1,j,Direction.MAP_RIGHT)):
					self.setWall(i,j,Direction.MAP_LEFT)
				if(i != self.xSize-1 and self.isWallExist(i+1,j,Direction.MAP_LEFT)):
					self.setWall(i,j,Direction.MAP_RIGHT)
				if(j != 0 and self.isWallExist(i,j-1,Direction.MAP_TOP)):
					self.setWall(i,j,Direction.MAP_BOTTOM)
				if(j != self.ySize-1 and self.isWallExist(i,j+1,Direction.MAP_BOTTOM)):
					self.setWall(i,j,Direction.MAP_TOP)

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
					if(self.isWallExist(columnNumber,rowNumber,Direction.MAP_LEFT)):
						sys.stdout.write("|")
						if(k==1 and self.isWallExist(columnNumber,rowNumber,Direction.MAP_BOTTOM)): sys.stdout.write("___")
						elif(k==1 and rowNumber==0): sys.stdout.write("___")
						else: sys.stdout.write("   ")
					else:
						if(k==1 and self.isWallExist(columnNumber,rowNumber,Direction.MAP_BOTTOM)): sys.stdout.write("____")
						elif(k==1 and rowNumber==0): sys.stdout.write("____")
						else: sys.stdout.write("    ")
				else:
					sys.stdout.write("|")
					if(k==1 and self.isWallExist(columnNumber,rowNumber,Direction.MAP_BOTTOM)): sys.stdout.write("___")
					elif(k==1 and rowNumber==0): sys.stdout.write("___")
					else: sys.stdout.write("   ")
				if(columnNumber==self.xSize-1):sys.stdout.write("|")
			print("")
