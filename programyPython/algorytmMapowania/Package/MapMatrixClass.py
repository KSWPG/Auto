import numpy as np
import sys

from DirectionEnum import DirectionEnum as Direction
from PositionClass import PositionClass

class MapMatrixClass():
	def __init__(self,xSize,ySize):
		self.xSize = xSize
		self.ySize = ySize
		self.mapMatrix = np.zeros((self.xSize,self.ySize),dtype=np.byte)

	def setWallsInContiguousField(self,position,direction):
		self.setWall(position,direction)

		positionForContiguousField = PositionClass()
		positionForContiguousField.copyFrom(position)
		directionForContiguousField = Direction.MAP_TOP

		if(direction == Direction.MAP_TOP):
			directionForContiguousField == Direction.MAP_BOTTOM
			positionForContiguousField.y = positionForContiguousField.y + 1
		elif(direction == Direction.MAP_BOTTOM):
			directionForContiguousField == Direction.MAP_TOP
			positionForContiguousField.y = positionForContiguousField.y - 1
		elif(direction == Direction.MAP_RIGHT):
			directionForContiguousField == Direction.MAP_LEFT
			positionForContiguousField.x = positionForContiguousField.x + 1
		elif(direction == Direction.MAP_LEFT):
			directionForContiguousField == Direction.MAP_RIGHT
			positionForContiguousField.x = positionForContiguousField.x - 1

		try:
			self.setWall(positionForContiguousField,directionForContiguousField)
		except:
			pass

	def setWall(self,position,direction):
		self.checkScopeOfIndex(position)
		if direction == Direction.MAP_TOP:
			self.mapMatrix[position.x][position.y] = self.mapMatrix[position.x][position.y] | 8
		elif direction == Direction.MAP_RIGHT:
			 self.mapMatrix[position.x][position.y] = self.mapMatrix[position.x][position.y] | 4
		elif direction == Direction.MAP_BOTTOM:
			self.mapMatrix[position.x][position.y] = self.mapMatrix[position.x][position.y] | 2
		elif direction == Direction.MAP_LEFT:
			self.mapMatrix[position.x][position.y] = self.mapMatrix[position.x][position.y] | 1
		else:
			raise Exception("Wrong parameter for direction")

	def removeWallsInContiguousField(self,position,direction):
		self.removeWall(position,direction)

		positionForContiguousField = PositionClass()
		positionForContiguousField.copyFrom(position)
		directionForContiguousField = Direction.MAP_TOP

		if(direction == Direction.MAP_TOP):
			directionForContiguousField = Direction.MAP_BOTTOM
			positionForContiguousField.y = positionForContiguousField.y + 1
		elif(direction == Direction.MAP_BOTTOM):
			directionForContiguousField = Direction.MAP_TOP
			positionForContiguousField.y = positionForContiguousField.y - 1
		elif(direction == Direction.MAP_RIGHT):
			directionForContiguousField = Direction.MAP_LEFT
			positionForContiguousField.x = positionForContiguousField.x + 1
		elif(direction == Direction.MAP_LEFT):
			directionForContiguousField = Direction.MAP_RIGHT
			positionForContiguousField.x = positionForContiguousField.x - 1

		try:
			self.removeWall(positionForContiguousField,directionForContiguousField)
		except:
			pass

	def removeWall(self,position,direction):
		self.checkScopeOfIndex(position)
		if direction == Direction.MAP_TOP:
			self.mapMatrix[position.x][position.y] = self.mapMatrix[position.x][position.y] & 247
		elif direction == Direction.MAP_RIGHT:
			 self.mapMatrix[position.x][position.y] = self.mapMatrix[position.x][position.y] & 251
		elif direction == Direction.MAP_BOTTOM:
			self.mapMatrix[position.x][position.y] = self.mapMatrix[position.x][position.y] & 253
		elif direction == Direction.MAP_LEFT:
			self.mapMatrix[position.x][position.y] = self.mapMatrix[position.x][position.y] & 254
		else:
			raise Exception("Wrong parameter for direction")

	def isWallExist(self,position,direction):
		self.checkScopeOfIndex(position)
		if direction == Direction.MAP_TOP :
			if self.mapMatrix[position.x][position.y] & 8 == 8:
				return True
		elif direction == Direction.MAP_RIGHT :
			if self.mapMatrix[position.x][position.y] & 4 == 4:
				return True
		elif direction == Direction.MAP_BOTTOM :
			if self.mapMatrix[position.x][position.y] & 2 == 2:
				return True
		elif direction == Direction.MAP_LEFT :
			if self.mapMatrix[position.x][position.y] & 1 == 1:
				return True
		else:
			raise Exception("Wrong parameter for direction")

		return False

	def setVisited(self,position):
		self.checkScopeOfIndex(position)
		self.mapMatrix[position.x][position.y] = self.mapMatrix[position.x][position.y] | 16

	def setUnVisited(self,position):
		self.checkScopeOfIndex(position)
		self.mapMatrix[position.x][position.y] = self.mapMatrix[position.x][position.y] & 239

	def wasVisited(self,position):
		self.checkScopeOfIndex(position)
		if self.mapMatrix[position.x][position.y] & 16 == 16:
			return True
		else:
			return False

	def setNotAvailable(self,position):
		self.checkScopeOfIndex(position)
		self.mapMatrix[position.x][position.y] = self.mapMatrix[position.x][position.y] | 32

	def setAvailable(self,position):
		self.checkScopeOfIndex(position)
		self.mapMatrix[position.x][position.y] = self.mapMatrix[position.x][position.y] & 223

	def isNotAvailable(self,position):
		self.checkScopeOfIndex(position)
		if self.mapMatrix[position.x][position.y] & 32 == 32:
			return True
		else:
			return False

	def checkScopeOfIndex(self,position):
		if(position.x < 0 or position.x >= self.xSize or position.y < 0 or position.y >= self.ySize):
			raise Exception("Matrix indexes outside the scope %i %i" % (position.x,position.y))

	def addNewRowIfNeeded(self,y,direction):
		if(direction == Direction.MAP_TOP and y == self.ySize-1):
			self.mapMatrix = np.insert(self.mapMatrix, [self.ySize],0,axis=1)
			self.ySize = self.ySize +1
			return True
		elif(direction == Direction.MAP_BOTTOM and y == 0):
			self.mapMatrix = np.insert(self.mapMatrix, [0],0,axis=1)
			self.ySize = self.ySize +1
			return True
		else:
			return False

	def addNewColumnIfNeeded(self,x,direction):
		if(direction == Direction.MAP_RIGHT and x == self.xSize-1):
			self.mapMatrix = np.insert(self.mapMatrix, [self.xSize],0,axis=0)
			self.xSize = self.xSize + 1
			return True
		elif(direction == Direction.MAP_LEFT and x == 0):
			self.mapMatrix = np.insert(self.mapMatrix, [0],0,axis=0)
			self.xSize = self.xSize + 1
			return True
		else:
			return False

	def findWayToNearestNoVisitedSpot(self,robotPosition):
		pathMap = np.zeros((self.xSize,self.ySize),dtype=np.byte)
		pathMap[robotPosition.x][robotPosition.y] = 1

		actualValue=1
		positionToCheck = PositionClass()
		foundPosition = PositionClass()
		endLoop=0

		while (endLoop==0):
			print("Cos")
			changeAmount=0
			position = PositionClass()
			for position.x in range(0,self.xSize):
				for position.y in range(0,self.ySize):
					if(pathMap[position.x][position.y] == actualValue):
						if(not self.isWallExist(position,Direction.MAP_LEFT)):
							if(pathMap[position.x-1][position.y] == 0):
								positionToCheck.copyFrom(position)
								positionToCheck.x = positionToCheck.x -1
								pathMap[positionToCheck.x][positionToCheck.y] = actualValue + 1
								changeAmount = changeAmount + 1
								if(not self.wasVisited(positionToCheck)):
									foundPosition.copyFrom(positionToCheck)
									endLoop = 1
									break
						if(not self.isWallExist(position,Direction.MAP_TOP)):
							if(pathMap[position.x][position.y + 1] == 0):
								positionToCheck.copyFrom(position)
								positionToCheck.y = positionToCheck.y + 1
								pathMap[positionToCheck.x][positionToCheck.y] = actualValue + 1
								changeAmount = changeAmount + 1
								if(not self.wasVisited(positionToCheck)):
									foundPosition.copyFrom(positionToCheck)
									endLoop = 1
									break
						if(not self.isWallExist(position,Direction.MAP_RIGHT)):
							if(pathMap[position.x+1][position.y] == 0):
								positionToCheck.copyFrom(position)
								positionToCheck.x = positionToCheck.x + 1
								pathMap[positionToCheck.x][positionToCheck.y] = actualValue + 1
								changeAmount = changeAmount + 1
								if(not self.wasVisited(positionToCheck)):
									foundPosition.copyFrom(positionToCheck)
									endLoop=1
									break
						if(not self.isWallExist(position,Direction.MAP_BOTTOM)):
							if(pathMap[position.x][position.y-1] == 0):
								positionToCheck.copyFrom(position)
								positionToCheck.y = positionToCheck.y - 1
								pathMap[positionToCheck.x][positionToCheck.y] = actualValue + 1
								changeAmount = changeAmount + 1
								if(not self.wasVisited(positionToCheck)):
									foundPosition.copyFrom(positionToCheck)
									endLoop = 1
									break
				if(endLoop!=0):break

			actualValue = actualValue + 1
			if(changeAmount==0):
				raise Exception("Not found anymore no visited spot")

		return self.findPathTo(robotPosition,foundPosition)

	def findWayToNearestNoVisitedSpot2(self,robotPosition):
		pathMap = np.zeros((self.xSize,self.ySize),dtype=np.byte)
		pathMap[robotPosition.x][robotPosition.y] = 1

		actualValue = 1
		foundPosition = PositionClass()
		endLoop = 0

		while (endLoop==0):
			changeAmount = 0
			position = PositionClass()
			for position.x in range(0,self.xSize):
				for position.y in range(0,self.ySize):
					if(pathMap[position.x][position.y] == actualValue):
						if position.course == 0:
							if(not self.isWallExist(position,Direction.MAP_LEFT)):
								if(pathMap[position.x-1][position.y] == 0):
									positionToCheck.copyFrom(position)
									positionToCheck.x = positionToCheck.x -1
									pathMap[positionToCheck.x][positionToCheck.y] = actualValue + 1
									changeAmount = changeAmount + 1
									if(not self.wasVisited(positionToCheck)):
										foundPosition.copyFrom(positionToCheck)
										endLoop = 1
										break
							if(not self.isWallExist(position,Direction.MAP_TOP)):
								if(pathMap[position.x][position.y + 1] == 0):
									positionToCheck.copyFrom(position)
									positionToCheck.y = positionToCheck.y + 1
									pathMap[positionToCheck.x][positionToCheck.y] = actualValue + 1
									changeAmount = changeAmount + 1
									if(not self.wasVisited(positionToCheck)):
										foundPosition.copyFrom(positionToCheck)
										endLoop = 1
										break
							if(not self.isWallExist(position,Direction.MAP_RIGHT)):
								if(pathMap[position.x+1][position.y] == 0):
									positionToCheck.copyFrom(position)
									positionToCheck.x = positionToCheck.x + 1
									pathMap[positionToCheck.x][positionToCheck.y] = actualValue + 1
									changeAmount = changeAmount + 1
									if(not self.wasVisited(positionToCheck)):
										foundPosition.copyFrom(positionToCheck)
										endLoop=1
										break
							if(not self.isWallExist(position,Direction.MAP_BOTTOM)):
								if(pathMap[position.x][position.y-1] == 0):
									positionToCheck.copyFrom(position)
									positionToCheck.y = positionToCheck.y - 1
									pathMap[positionToCheck.x][positionToCheck.y] = actualValue + 1
									changeAmount = changeAmount + 1
									if(not self.wasVisited(positionToCheck)):
										foundPosition.copyFrom(positionToCheck)
										endLoop = 1
										break
						elif position.course == 90:
							if(not self.isWallExist(position,Direction.MAP_TOP)):
								if(pathMap[position.x][position.y + 1] == 0):
									positionToCheck.copyFrom(position)
									positionToCheck.y = positionToCheck.y + 1
									pathMap[positionToCheck.x][positionToCheck.y] = actualValue + 1
									changeAmount = changeAmount + 1
									if(not self.wasVisited(positionToCheck)):
										foundPosition.copyFrom(positionToCheck)
										endLoop = 1
										break
							if(not self.isWallExist(position,Direction.MAP_RIGHT)):
								if(pathMap[position.x+1][position.y] == 0):
									positionToCheck.copyFrom(position)
									positionToCheck.x = positionToCheck.x + 1
									pathMap[positionToCheck.x][positionToCheck.y] = actualValue + 1
									changeAmount = changeAmount + 1
									if(not self.wasVisited(positionToCheck)):
										foundPosition.copyFrom(positionToCheck)
										endLoop=1
										break
							if(not self.isWallExist(position,Direction.MAP_BOTTOM)):
								if(pathMap[position.x][position.y-1] == 0):
									positionToCheck.copyFrom(position)
									positionToCheck.y = positionToCheck.y - 1
									pathMap[positionToCheck.x][positionToCheck.y] = actualValue + 1
									changeAmount = changeAmount + 1
									if(not self.wasVisited(positionToCheck)):
										foundPosition.copyFrom(positionToCheck)
										endLoop = 1
										break
							if(not self.isWallExist(position,Direction.MAP_LEFT)):
								if(pathMap[position.x-1][position.y] == 0):
									positionToCheck.copyFrom(position)
									positionToCheck.x = positionToCheck.x - 1
									pathMap[positionToCheck.x][positionToCheck.y] = actualValue + 1
									changeAmount = changeAmount + 1
									if(not self.wasVisited(positionToCheck)):
										foundPosition.copyFrom(positionToCheck)
										endLoop = 1
										break
						elif position.course == 180:
							if(not self.isWallExist(position,Direction.MAP_RIGHT)):
								if(pathMap[position.x+1][position.y] == 0):
									positionToCheck.copyFrom(position)
									positionToCheck.x = positionToCheck.x + 1
									pathMap[positionToCheck.x][positionToCheck.y] = actualValue + 1
									changeAmount = changeAmount + 1
									if(not self.wasVisited(positionToCheck)):
										foundPosition.copyFrom(positionToCheck)
										endLoop=1
										break
							if(not self.isWallExist(position,Direction.MAP_BOTTOM)):
								if(pathMap[position.x][position.y-1] == 0):
									positionToCheck.copyFrom(position)
									positionToCheck.y = positionToCheck.y - 1
									pathMap[positionToCheck.x][positionToCheck.y] = actualValue + 1
									changeAmount = changeAmount + 1
									if(not self.wasVisited(positionToCheck)):
										foundPosition.copyFrom(positionToCheck)
										endLoop = 1
										break
							if(not self.isWallExist(position,Direction.MAP_LEFT)):
								if(pathMap[position.x-1][position.y] == 0):
									positionToCheck.copyFrom(position)
									positionToCheck.x = positionToCheck.x - 1
									pathMap[positionToCheck.x][positionToCheck.y] = actualValue + 1
									changeAmount = changeAmount + 1
									if(not self.wasVisited(positionToCheck)):
										foundPosition.copyFrom(positionToCheck)
										endLoop = 1
										break
							if(not self.isWallExist(position,Direction.MAP_TOP)):
								if(pathMap[position.x][position.y + 1] == 0):
									positionToCheck.copyFrom(position)
									positionToCheck.y = positionToCheck.y + 1
									pathMap[positionToCheck.x][positionToCheck.y] = actualValue + 1
									changeAmount = changeAmount + 1
									if(not self.wasVisited(positionToCheck)):
										foundPosition.copyFrom(positionToCheck)
										endLoop = 1
										break
						elif position.course ==270:
							if(not self.isWallExist(position,Direction.MAP_BOTTOM)):
								if(pathMap[position.x][position.y-1] == 0):
									positionToCheck.copyFrom(position)
									positionToCheck.y = positionToCheck.y - 1
									pathMap[positionToCheck.x][positionToCheck.y] = actualValue + 1
									changeAmount = changeAmount + 1
									if(not self.wasVisited(positionToCheck)):
										foundPosition.copyFrom(positionToCheck)
										endLoop = 1
										break
							if(not self.isWallExist(position,Direction.MAP_LEFT)):
								if(pathMap[position.x-1][position.y] == 0):
									positionToCheck.copyFrom(position)
									positionToCheck.x = positionToCheck.x - 1
									pathMap[positionToCheck.x][positionToCheck.y] = actualValue + 1
									changeAmount = changeAmount + 1
									if(not self.wasVisited(positionToCheck)):
										foundPosition.copyFrom(positionToCheck)
										endLoop = 1
										break
							if(not self.isWallExist(position,Direction.MAP_TOP)):
								if(pathMap[position.x][position.y + 1] == 0):
									positionToCheck.copyFrom(position)
									positionToCheck.y = positionToCheck.y + 1
									pathMap[positionToCheck.x][positionToCheck.y] = actualValue + 1
									changeAmount = changeAmount + 1
									if(not self.wasVisited(positionToCheck)):
										foundPosition.copyFrom(positionToCheck)
										endLoop = 1
										break
							if(not self.isWallExist(position,Direction.MAP_RIGHT)):
								if(pathMap[position.x+1][position.y] == 0):
									positionToCheck.copyFrom(position)
									positionToCheck.x = positionToCheck.x + 1
									pathMap[positionToCheck.x][positionToCheck.y] = actualValue + 1
									changeAmount = changeAmount + 1
									if(not self.wasVisited(positionToCheck)):
										foundPosition.copyFrom(positionToCheck)
										endLoop=1
										break


				if(endLoop!=0):break
			actualValue = actualValue + 1
			if(changeAmount==0):
				raise Exception("Not found anymore no visited spot")

		return self.findPathTo(robotPosition,foundPosition)

	def findPathTo(self,fromPosition,toPosition):
		pathMap = np.zeros((self.xSize,self.ySize),dtype=np.byte)
		pathMap[toPosition.x][toPosition.y] = 1
		actualValue = 1
		endLoop=0
		while (endLoop==0):
			position = PositionClass()
			for position.x in range(0,self.xSize):
				for position.y in range(0,self.ySize):
					if(pathMap[position.x][position.y] == actualValue):
						if(position.x != 0 and not self.isWallExist(position,Direction.MAP_LEFT)):
							positionToCheck = PositionClass()
							positionToCheck.copyFrom(position)
							positionToCheck.x = positionToCheck.x - 1
							if(pathMap[positionToCheck.x][positionToCheck.y]==0):
								pathMap[positionToCheck.x][positionToCheck.y] = actualValue + 1
								if(positionToCheck.x == fromPosition.x and positionToCheck.y == fromPosition.y):
									endLoop = 1
									break
						if(position.y != self.ySize-1 and not self.isWallExist(position,Direction.MAP_TOP)):
							positionToCheck = PositionClass()
							positionToCheck.copyFrom(position)
							positionToCheck.y = positionToCheck.y + 1
							if(pathMap[positionToCheck.x][positionToCheck.y]==0):
								pathMap[positionToCheck.x][positionToCheck.y] = actualValue + 1
								if(positionToCheck.x == fromPosition.x and positionToCheck.y == fromPosition.y):
									endLoop = 1
									break
						if(position.x != self.xSize-1 and not self.isWallExist(position,Direction.MAP_RIGHT)):
							positionToCheck = PositionClass()
							positionToCheck.copyFrom(position)
							positionToCheck.x = positionToCheck.x + 1
							if(pathMap[positionToCheck.x][positionToCheck.y]==0):
								pathMap[positionToCheck.x][positionToCheck.y] = actualValue + 1
								if(positionToCheck.x == fromPosition.x and positionToCheck.y == fromPosition.y):
									endLoop = 1
									break
						if(position.y !=0 and not self.isWallExist(position,Direction.MAP_BOTTOM)):
							positionToCheck = PositionClass()
							positionToCheck.copyFrom(position)
							positionToCheck.y = positionToCheck.y - 1
							if(pathMap[positionToCheck.x][positionToCheck.y]==0):
								pathMap[positionToCheck.x][positionToCheck.y] = actualValue + 1
								if(positionToCheck.x == fromPosition.x and positionToCheck.y == fromPosition.y):
									endLoop = 1
									break
				if(endLoop!=0):
					break
			actualValue = actualValue + 1

		#print pathMap
		return pathMap

	def completeMapAfterMapping(self):
		position = PositionClass()
		for position.x in range(0,self.xSize):
			for position.y in range(0,self.ySize):
				if(not self.wasVisited(position)):
					self.setNotAvailable(position)

				positionToCheck = PositionClass()

				positionToCheck.copyFrom(position)
				positionToCheck.x = position.x - 1
				if(position.x != 0 and self.isWallExist(positionToCheck,Direction.MAP_RIGHT)):
					self.setWall(position,Direction.MAP_LEFT)

				positionToCheck.copyFrom(position)
				positionToCheck.x = position.x + 1
				if(position.x != self.xSize-1 and self.isWallExist(positionToCheck,Direction.MAP_LEFT)):
					self.setWall(position,Direction.MAP_RIGHT)

				positionToCheck.copyFrom(position)
				positionToCheck.y = position.y - 1
				if(position.y != 0 and self.isWallExist(positionToCheck,Direction.MAP_TOP)):
					self.setWall(position,Direction.MAP_BOTTOM)

				positionToCheck.copyFrom(position)
				positionToCheck.y = position.y + 1
				if(position.y != self.ySize-1 and self.isWallExist(positionToCheck,Direction.MAP_BOTTOM)):
					self.setWall(position,Direction.MAP_TOP)

	def drawMap(self):
		sys.stdout.flush()

		for k in range(0,self.xSize):
			sys.stdout.write('____')
		print("")
		for rowNumber in range(self.ySize-1,-1,-1):
			self.drawMatrixRow(rowNumber)

	def drawMatrixRow(self,rowNumber):
		for k in range(0,2):
			position = PositionClass()
			position.y = rowNumber
			for position.x in range(0,self.xSize):
				if(position.x is not 0):
					if(self.isWallExist(position,Direction.MAP_LEFT)):
						sys.stdout.write("|")
						if(k==1 and self.isWallExist(position,Direction.MAP_BOTTOM)):
							sys.stdout.write("___")
						elif(k==1 and position.y==0):
							sys.stdout.write("___")
						else:
							sys.stdout.write("   ")
					else:
						if(k==1 and self.isWallExist(position,Direction.MAP_BOTTOM)): sys.stdout.write("____")
						elif(k==1 and position.y==0): sys.stdout.write("____")
						else: sys.stdout.write("    ")
				else:
					sys.stdout.write("|")
					if(k==1 and self.isWallExist(position,Direction.MAP_BOTTOM)):
						sys.stdout.write("___")
					elif(k==1 and position.y==0):
						sys.stdout.write("___")
					else:
						sys.stdout.write("   ")
				if(position.x==self.xSize-1):
					sys.stdout.write("|")
			print("")
