import numpy as np
#import RPi.GPIO as GPIO

#from Package import MotorControl
from MapMatrixClass import MapMatrixClass
from SimulationMapMatrixClass import SimulationMapMatrixClass
from PositionClass import PositionClass
from DirectionEnum import DirectionEnum as Direction


class RobotClass:
	def __init__(self):
		#GPIO.setmode(GPIO.BCM)

		#inicjalizacja silnikow
		#self.motors = MotorControl(23,12,22,13)

		#inicjalizacja sensorow
		##

		#wykorzystwane tylko do testowania algorytmu potem do usuniecia
		self.simulationMap = SimulationMapMatrixClass(10,10)

		self.position = PositionClass()
		self.moves=0
		self.map = MapMatrixClass(1,1)

	def checkSensor(self):
		#do testow, pozniej do zamienia przez odczyty z czujnikow ktory bedzie trzeba uzaleznic od wartosci self.position.course
		if self.simulationMap.isWallExist(self.position,Direction.MAP_TOP):
			self.map.setWallsInContiguousField(self.position,Direction.MAP_TOP)
		elif self.map.addNewRowIfNeeded(self.position.y,Direction.MAP_TOP):
			pass

		if self.simulationMap.isWallExist(self.position,Direction.MAP_RIGHT):
			self.map.setWallsInContiguousField(self.position,Direction.MAP_RIGHT)
		elif self.map.addNewColumnIfNeeded(self.position.x,Direction.MAP_RIGHT):
			pass

		if self.simulationMap.isWallExist(self.position,Direction.MAP_BOTTOM):
			self.map.setWallsInContiguousField(self.position,Direction.MAP_BOTTOM)
		elif self.map.addNewRowIfNeeded(self.position.y,Direction.MAP_BOTTOM):
			self.position.y = self.position.y + 1

		if self.simulationMap.isWallExist(self.position,Direction.MAP_LEFT):
			self.map.setWallsInContiguousField(self.position,Direction.MAP_LEFT)
		elif self.map.addNewColumnIfNeeded(self.position.x,Direction.MAP_LEFT):
			self.position.x = self.position.x +1

		self.map.setVisited(self.position)

	def goForward(self):
		#motors.ForwardOneField
		self.position.goOneFieldForward()

	def goRight(self):
		#motors.turnRight()
		self.position.addToCourse(90)
		self.goForward()

	def goBack(self):
		#motors.turnBack()
		self.position.addToCourse(180)
		self.goForward()

	def goLeft(self):
		#motors.turnLeft()
		self.position.addToCourse(270)
		self.goForward()

	def goByPath(self,pathMap):
		while (pathMap[self.position.x][self.position.y] != 1):
			actualValue = pathMap[self.position.x][self.position.y]
			if(self.position.x != self.map.xSize-1 and pathMap[self.position.x+1][self.position.y] == actualValue-1):
				if self.position.course == 0:
					self.goRight()
				elif self.position.course == 90:
					self.goForward()
				elif self.position.course == 180:
					self.goLeft()
				elif self.position.course == 270:
					self.goBack()
			elif(self.position.x != 0 and pathMap[self.position.x-1][self.position.y] == actualValue-1):
				if self.position.course == 0:
					self.goLeft()
				elif self.position.course == 90:
					self.goBack()
				elif self.position.course == 180:
					self.goRight()
				elif self.position.course == 270:
					self.goForward()
			elif(self.position.y != self.map.ySize-1 and pathMap[self.position.x][self.position.y+1] == actualValue-1):
				if self.position.course == 0:
					self.goForward()
				elif self.position.course == 90:
					self.goLeft()
				elif self.position.course == 180:
					self.goBack()
				elif self.position.course == 270:
					self.goRight()
			elif(self.position.y != 0 and pathMap[self.position.x][self.position.y-1] == actualValue-1):
				if self.position.course == 0:
					self.goBack()
				elif self.position.course == 90:
					self.goRight()
				elif self.position.course == 180:
					self.goForward()
				elif self.position.course == 270:
					self.goLeft()

			self.moves=self.moves+1
