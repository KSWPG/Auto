import numpy as np
import sys

from DirectionEnum import DirectionEnum as Direction
from PositionClass import PositionClass
from FindWayClass import *

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
			self.setWall(positionForContiguousField,directionForContiguousField)
		except Exception as e:
			#print("Wall: %s" % e)
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
		except Exception as e:
			#print("Remove wall: %s" % e)
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
		if(direction == Direction.MAP_TOP):
			if self.mapMatrix[position.x][position.y] & 8 == 8:
				return True
		elif(direction == Direction.MAP_RIGHT):
			if self.mapMatrix[position.x][position.y] & 4 == 4:
				return True
		elif(direction == Direction.MAP_BOTTOM):
			if self.mapMatrix[position.x][position.y] & 2 == 2:
				return True
		elif(direction == Direction.MAP_LEFT):
			if self.mapMatrix[position.x][position.y] & 1 == 1:
				return True
		else:
			raise Exception("Wrong parameter for direction", direction)

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
		findWay = FindWayClass(self)
		return findWay.findWayToNearestNoVisitedSpot(robotPosition)

	def findWayToNearestNoVisitedSpot2(self,robotPosition):
		findWay = FindWayClass(self)
		return findWay.findWayToNearestNoVisitedSpot2(robotPosition)

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
